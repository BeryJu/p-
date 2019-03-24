## Initial Configuration

After you've installed p2 and created your superuser, there is some configuration needed to make p2 work.

The configuration is done in `/etc/p2/config.yml`. The two most important settings are called `external_url` and `domains`.

 - `external_url` dictates which URL should be used for link generation. This setting must include the protocol, e.g. `https://i.beryju.org`
 - `domains` is a list of domains which p2 can be accessed under. If you're directly accessing p2 without a reverse-proxy, this must contain the DNS name used to access p2. If you're using a reverse-proxy, add the same value here as you've set in `proxy_pass`

You can also optionally enable `error_report_enabled`, which sends errors directly to `sentry.services.beryju.org`.

If you prefer shorter links, you can adjust the setting `default_return_view`, which defaults to using the SHA256 of the uploaded file.
The length of links is as following:

| Function          | Length |
|-------------------|--------|
| view_sha512_short | 16     |
| view_md5          | 32     |
| view_sha256       | 64     |
| view_sha512       | 128    |
