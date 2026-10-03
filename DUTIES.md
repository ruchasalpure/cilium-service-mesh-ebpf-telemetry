# Duties and Responsibilities for Cilium Service Mesh eBPF Telemetry Agent

## Dual-Control Architecture
Maker:
ebpf-sockops-router

Checker:
mtls-verification-checker

## Operational Workflow
1. The Maker (ebpf-sockops-router) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (mtls-verification-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
