 Download the CRDB client, if you haven’t already done it before.
$ErrorActionPreference = "Stop"; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $ProgressPreference = 'SilentlyContinue'; mkdir -p $env:appdata/cockroach; Invoke-WebRequest -Uri https://binaries.cockroachdb.com/cockroach-v21.1.4.windows-6.2-amd64.zip -OutFile cockroach.zip; Expand-Archive -Path cockroach.zip; Copy-Item cockroach/cockroach-v21.1.4.windows-6.2-amd64/cockroach.exe -Destination $env:appdata/cockroach; $Env:PATH += ";$env:appdata/cockroach"
Copy
2. If you haven’t already, download the CA certificate using this command:
mkdir -p $env:appdata\.postgresql\; Invoke-WebRequest -Uri https://cockroachlabs.cloud/clusters/6c0b6c39-4a8e-4586-aa97-2305471cca6a/cert -OutFile $env:appdata\.postgresql\root.crt
Copy
3. Run this command to connect to your database.
Your password will be provided only once. Copy the code below and save it in a secure location.
cockroach sql --url "postgresql://rakesh:REVEAL_PASSWORD@free-tier6.gcp-asia-southeast1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=$env:appdata\.postgresql\root.crt&options=--cluster%3Dlumpy-whale-874"
