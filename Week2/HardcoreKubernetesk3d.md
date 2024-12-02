 # Install

To run a highly secure version of k3d using hardened images, you can leverage Chainguard Images, which provide minimal, security-hardened container images. Here's a robust approach to setting up k3d with enhanced security:
Using Chainguard Images for k3d
Create a k3d configuration file:
Create a YAML file named k3d-secure.yaml with the following content:

```k3d cluster create --config k3d-secure.yaml```

Configure system mounts:
After creating the cluster, run the following command to set up the required system mounts:
bash
```for node in $(kubectl get nodes -o jsonpath='{.items[*].metadata.name}'); do
  docker exec -i $node /bin/sh <<-EOF
    mount bpffs -t bpf /sys/fs/bpf
    mount --make-shared /sys/fs/bpf
    mkdir -p /run/cilium/cgroupv2
    mount -t cgroup2 none /run/cilium/cgroupv2
    mount --make-shared /run/cilium/cgroupv2/
EOF
done
```

### Enhancing Security with Cilium
To further harden your k3d cluster, you can install Cilium using Chainguard Images:
Set environment variables for Cilium components:
```bash
brew install cilium-cli
export AGENT_IMAGE=cgr.dev/chainguard/cilium-agent:latest
export HUBBLE_RELAY_IMAGE=cgr.dev/chainguard/cilium-hubble-relay:latest
export HUBBLE_UI_IMAGE=cgr.dev/chainguard/cilium-hubble-ui:latest
export HUBBLE_UI_BACKEND_IMAGE=cgr.dev/chainguard/cilium-hubble-ui-backend:latest
export OPERATOR_IMAGE=cgr.dev/chainguard/cilium-operator-generic:latest
```

## Install Cilium:
```bash
cilium install \
  --helm-set hubble.relay.enabled=true \
  --helm-set hubble.ui.enabled=true \
  --helm-set image.override=$AGENT_IMAGE \
  --helm-set hubble.relay.image.override=$HUBBLE_RELAY_IMAGE \
  --helm-set hubble.ui.frontend.image.override=$HUBBLE_UI_IMAGE \
  --helm-set hubble.ui.backend.image.override=$HUBBLE_UI_BACKEND_IMAGE \
  --helm-set operator.image.override=$OPERATOR_IMAGE
```



