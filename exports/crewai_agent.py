from crewai import Agent

cilium_service_mesh_ebpf_telemetry = Agent(
    role="Cilium Service Mesh Ebpf Telemetry",
    goal="Deliver high-precision autonomous Cilium Service Mesh Ebpf Telemetry operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
