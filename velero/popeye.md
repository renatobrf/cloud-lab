# Popeye: Kubernetes Live Cluster Linter

## Architecture assessment

### Executive summary

Popeye is a read-only Kubernetes operations linter. It connects to a live cluster through Kubernetes credentials, inspects selected deployed resources, evaluates them against built-in checks and optional Spinach YAML configuration, then emits a report. It is best treated as a lightweight, periodic health-assessment tool—not as a policy enforcement engine, remediation controller, static manifest analyzer, or security/compliance scanner.

For this cloud lab, Popeye can provide an additional operational visibility layer alongside workload and backup tooling. It can identify issues in the cluster's current state, but it does not validate Velero backup contents or prove that a restore will succeed; those require separate backup and restore tests.

### Logical architecture and data flow

```text
Operator / scheduled job
          |
          | CLI flags, kubeconfig context, optional Spinach YAML
          v
      Popeye process
          |
          | Kubernetes API reads (get/list)
          | Optional metrics API reads
          v
 Live cluster resources and metrics
          |
          v
 Resource-specific linters and configured exclusions/thresholds
          |
          v
 Findings, severity counts, and cluster score
          |
          +--> terminal / YAML / JSON / HTML / JUnit / score
          +--> saved report (local filesystem or S3-compatible object store)
          +--> Prometheus Pushgateway metrics
```

The diagram describes the documented operating model rather than an assertion about internal implementation details. Popeye scans resources as deployed, not manifests on disk. Its checks cover a curated set of Kubernetes resource types, including nodes, pods, services, workloads, storage resources, RBAC objects, and networking resources. Metrics-based utilization checks depend on accessible metrics APIs, typically supplied by metrics-server.

### Deployment and integration options

- **Operator-run CLI:** Uses the current kubeconfig context, with options to select another context or namespace. Useful for interactive investigations and ad hoc assessments.
- **In-cluster Job or CronJob:** Runs on a schedule using a dedicated ServiceAccount. This provides repeatable assessments without depending on an operator's workstation, but requires careful RBAC and report retention configuration.
- **Reports:** Supports standard terminal output plus YAML, JSON, HTML, JUnit, Prometheus, and score formats. Reports can be saved locally or sent to S3-compatible storage. Prometheus metrics are pushed to a configured Pushgateway; Popeye is not itself a continuously running metrics endpoint.
- **Spinach YAML:** Allows thresholds, severity overrides, registry expectations, and resource/code exclusions to be configured. Exclusions can hide relevant findings, so they should be reviewed and version controlled.

### Security and access assessment

Popeye is documented as read-only: it does not change Kubernetes resources. Its effective access is nevertheless security-sensitive because it reads live cluster state and the report may include names, configuration details, and findings about resources.

The upstream sample RBAC includes `get` and `list` permissions for Secrets, as well as many namespaced and cluster-scoped resources. Treat this as a starting point only. Before deployment:

1. Review the exact resources and API groups queried by the Popeye version in use, then grant only the required `get`/`list` permissions.
2. Restrict namespaced scans where possible; recognize that node and cluster-scoped checks require cluster-scoped access.
3. Avoid broad human-admin credentials for routine scans. Use a dedicated ServiceAccount in-cluster or a narrowly scoped kubeconfig identity.
4. Protect report files and object-store destinations as sensitive operational data; apply access controls, retention limits, and encryption appropriate to the environment.
5. Pin the Popeye image/version and validate upgrades against a non-production cluster before changing scheduled scans.
6. Review Spinach exclusions and regular expressions: overly broad exclusions can suppress findings.

### Operational considerations and limitations

- **Snapshot, not continuous monitoring:** A scan reflects the state observed during that run. It does not replace Kubernetes monitoring, alerting, admission controls, or runtime security tooling.
- **Curated coverage:** Popeye checks only the resource types and conditions implemented by its linters. A clean score does not establish full security, reliability, or compliance.
- **Live-cluster only:** It is complementary to static manifest and IaC analysis; it does not lint unapplied YAML.
- **Metrics are optional and conditional:** Resource-utilization analysis requires metrics availability and should be interpreted as a point-in-time signal, not capacity planning by itself.
- **Exit codes affect automation:** The README notes that lint findings can result in a non-zero exit code. For scheduled Kubernetes Jobs, determine whether that behavior should mark the Job failed; the upstream example uses `--force-exit-zero` to avoid that outcome. Preserve and inspect the report even if the exit status is normalized.
- **RBAC and API compatibility:** Missing permissions or unsupported cluster/API versions can lead to incomplete scans or errors. Validate required access and scan output for the deployed Popeye and Kubernetes versions.
- **No automatic remediation:** Findings require human or separately automated follow-up. This separation is useful for safety, but means Popeye alone does not close the operational loop.

### Recommendation

Use Popeye as a scheduled, read-only assessment with a dedicated identity, least-privilege RBAC, pinned image, and retained JSON or HTML reports. Start with a broad baseline scan, review findings and exclusions with cluster owners, then introduce narrowly scoped configuration and thresholds. If metrics are available, use utilization findings as investigation prompts rather than automatic scaling or right-sizing decisions.

Keep Popeye separate from backup validation: pair its cluster-health reports with routine Velero backup-status checks and restore drills. Do not interpret a favorable Popeye score as evidence that backups are recoverable or that the cluster meets a formal security baseline.

### References

- [Popeye upstream README](https://github.com/derailed/popeye/blob/master/README.md) — capabilities, supported checks, command options, outputs, Spinach configuration, in-cluster operation, and sample RBAC.
- [Popeye linter codes](https://github.com/derailed/popeye/blob/master/docs/codes.md) — reference for interpreting reported findings.
