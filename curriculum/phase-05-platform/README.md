# Phase 5: AI Platform Engineering

## Overview

Weeks 19-22; 32-48 hours, target 40. Prerequisites: Phase 4 sign-off, the Phase 3 server,
and distributed-systems reasoning. Build a small serving control layer with explicit
reliability, deployment, and operational behavior rather than a general-purpose platform.

Use local services and a minimal local Kubernetes CPU workload. Keep MPS/Ollama inference
on the macOS host; document the container-to-host connection instead of assuming containers
can use MPS. Verify Docker and local cluster readiness before deployment exercises.

## Learning objectives

- **Conceptual:** explain gateways, routing/load balancing, authentication/authorization,
  rate limits, quotas, cost accounting, lifecycle management, and observability.
- **Implementation:** extend the server with gateway policies, metrics/traces, reliability
  handling, and reproducible container/local Kubernetes deployment.
- **Performance:** analyze queue/capacity signals, rate enforcement, scaling behavior,
  latency distributions, and failure effects.
- **System design:** justify routing, deadlines, retry limits, scaling signals, and
  operational boundaries; compare a small custom service with Ray-style scheduling.

## Weekly milestones and exercise previews

| Week | Starting point and planned exercise | Verification / expected observation |
| --- | --- | --- |
| 19 | Extend Project 2 with routing, load balancing, auth/authz | Policies apply to the correct caller/backend; document trust boundaries |
| 20 | Add quotas, rates, cost estimates, deadlines, and failure policies | Limits are enforced; retries remain bounded and appropriate for streaming |
| 21 | Containerize control services; deploy a minimal CPU service locally | Verify readiness/lifecycle and reason about autoscaling signals |
| 22 | Add metrics/traces and inject failures | Correlate request flow and failures; assess architecture and limits |

Budget 8-12 hours weekly. Prepare exact exercise contracts and deployment choices when
starting the phase rather than adding unused infrastructure during bootstrap.

## Study materials

Links/sections checked 2026-11-01; reading/practice time is included in the phase budget.

| Resource | Classification and activity | Hours | Expected takeaway |
| --- | --- | --- | --- |
| [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/), deploy/expose/scale/update | Required; selected local exercises | 3 | Understand deployment objects, service access, replicas, and updates |
| [Prometheus histograms and summaries](https://prometheus.io/docs/practices/histograms/) | Required; reading and metric design | 1 | Measure and aggregate latency distributions correctly |
| [Ray Serve](https://docs.ray.io/en/latest/serve/index.html) | Optional; architecture and scheduling comparison | 2 | Compare deployment, scheduling, and scaling abstractions |

## Key concepts

Separate rate from concurrent admission, authentication from authorization, and estimated
cost from actual charges. Distinguish model readiness from process liveness and request
deadlines from per-attempt timeouts. Define metric label cardinality and trace propagation.
Treat autoscaling as a delayed control loop with capacity and queueing consequences.

## Project 4, first increment: AI Serving Platform

Reuse Project 2. Minimum increment: gateway policies, local routing, limits/security,
failure handling, metrics/traces, and a local deployment demonstration. Work fits within
this phase's 32-48 hours; integration/hardening continues in Phase 6, not a second server.

Test policy enforcement, backend failure, deadline/cancellation propagation, and trace
continuity. Deliver an architecture sketch, deployment instructions, and failure evidence.
Advanced orchestration, service meshes, paid backends, and elaborate identity systems are
optional extensions, not baseline completion requirements.

## Industry and research connections

Connect the gateway's policies with Kubernetes lifecycle/scaling primitives, Prometheus
measurement, and Ray Serve abstractions. Explain which mechanisms are unnecessary for a
small workload, not merely which ones exist in a popular production platform.

## Assessment and sign-off

Demonstrate rate/quota enforcement, backend-failure behavior, and trace continuity. Explain
routing/scaling trade-offs and diagnose a failure using evidence. Use the
[shared rubric](../../AGENTS.md), remediate gaps, then request `SIGN OFF: Phase 5` before
the capstone. Record module approvals and unresolved limitations separately.
