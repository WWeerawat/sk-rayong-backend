from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = "skrayongblobstorage"

    account_key = "SRIgCwfJf6xBQJRKKKdvJrrUEuu3tG5EGwvslKN68Ug/zoDFTdUmhCfWY6ExHvkdCAUrZNr43w+RgyxvwMGHVQ=="  # Must be replaced by your <storage_account_key>
    azure_container = "media"
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = "skrayongblobstorage"

    account_key = "SRIgCwfJf6xBQJRKKKdvJrrUEuu3tG5EGwvslKN68Ug/zoDFTdUmhCfWY6ExHvkdCAUrZNr43w+RgyxvwMGHVQ=="  # Must be replaced by your <storage_account_key>
    azure_container = "static"
    expiration_secs = None
