# Python Prometheus API 

A simple python wrapper for Prometheus HTTP API

### Usage Examples

##### Import package
```
from promapi import prometheus
```

##### Set Prometheus Endpoint
```
prometheus.set_endpoint("http://localhost",9090)
```

##### Instant Query
```
result = prometheus.query_instant("rate(node_network_receive_bytes_total{job=~\"node-exporter\"}[5m])")
print(result)
```

##### Range Query
```
result = prometheus.query_range("rate(node_network_receive_bytes_total{job=~\"node-exporter\"}[5m])", start=1562261669, end=1562262242, step=60)
print(result)
```

##### Query Series by Label Matcher
```
result = prometheus.query_metadata_series("process_start_time_seconds{job=\"prometheus\"}")
print(result)
```

##### Get Label Names
```
result = prometheus.query_metadata_series("up")
print(result)
```

##### Query Label Names
```
result = prometheus.query_label_names()
print(result)
```

##### Query Label Values
```
result = prometheus.query_label_values('job')
print(result)
```

##### Query Targets
```
result = prometheus.query_targets()
print(result)
```

##### Query Rules
```
result = prometheus.query_rules()
print(result)
```

##### Query Alerts
```
result = prometheus.query_alerts()
print(result)
```

##### Query Target Metadata
```
result = prometheus.query_target_metadata("{instance=\"host.docker.internal:9100\"}")
print(result)
```

##### Query Alertmanagers
```
result = prometheus.query_alertmanagers()
print(result)
```

##### Query Status Config
```
result = prometheus.query_status_config()
print(result)
```

##### Query Status Flags
```
result = prometheus.query_status_flags()
print(result)
```

##### Create Snapshot of Current Data
```
result = prometheus.create_snapshot(skip_head=False)
print(result)
```