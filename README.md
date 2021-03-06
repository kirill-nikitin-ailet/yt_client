# yt-client
YouTrack issue tracking and project management system

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2021.2
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import yt_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import yt_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import yt_client
from yt_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://youtrack.intrtl.com:443/api
# See configuration.py for a list of all supported configuration parameters.
configuration = yt_client.Configuration(
    host = "https://youtrack.intrtl.com:443/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (YouTrack permanent token): permanentToken
configuration = yt_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with yt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yt_client.DefaultApi(api_client)
    categories = 'categories_example' # str |  (optional)
reverse = True # bool | Indicates whether the order of returning activities is from newest to oldest or the opposite. If \"false\", then the oldest activity item that matches a selected filter is returned first. If \"true\", then the newest activity is returned first. By default, \"false\". (optional)
start = 'start_example' # str | Start timestamp of the time interval the activity timestamp belongs to. If the parameter is not set, it is considered to be 0. (optional)
end = 'end_example' # str | End timestamp of the time interval the activity timestamp belongs to. If the parameter is not set, it is considered as Long.MAX_VALUE. (optional)
author = 'author_example' # str | Parameter to filter activities by the author. The database id or login, or Hub id, or 'me' for the current logged in user could be specified. (optional)
issue_query = 'issue_query_example' # str | Issues search query. Read more about <a href=\"Search-and-Command-Attributes.xml\">search syntax</a>. (optional)
fields = '$type,added,author($type,id,login,name,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp' # str |  (optional)
skip = 56 # int |  (optional)
top = 56 # int |  (optional)

    try:
        api_response = api_instance.activities_get(categories=categories, reverse=reverse, start=start, end=end, author=author, issue_query=issue_query, fields=fields, skip=skip, top=top)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->activities_get: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://youtrack.intrtl.com:443/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**activities_get**](docs/DefaultApi.md#activities_get) | **GET** /activities | 
*DefaultApi* | [**activities_id_get**](docs/DefaultApi.md#activities_id_get) | **GET** /activities/{id} | 
*DefaultApi* | [**activities_page_get**](docs/DefaultApi.md#activities_page_get) | **GET** /activitiesPage | 
*DefaultApi* | [**admin_custom_field_settings_bundles_build_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_build_get) | **GET** /admin/customFieldSettings/bundles/build | 
*DefaultApi* | [**admin_custom_field_settings_bundles_build_id_delete**](docs/DefaultApi.md#admin_custom_field_settings_bundles_build_id_delete) | **DELETE** /admin/customFieldSettings/bundles/build/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_build_id_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_build_id_get) | **GET** /admin/customFieldSettings/bundles/build/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_build_id_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_build_id_post) | **POST** /admin/customFieldSettings/bundles/build/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_build_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_build_post) | **POST** /admin/customFieldSettings/bundles/build | 
*DefaultApi* | [**admin_custom_field_settings_bundles_enum_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_enum_get) | **GET** /admin/customFieldSettings/bundles/enum | 
*DefaultApi* | [**admin_custom_field_settings_bundles_enum_id_delete**](docs/DefaultApi.md#admin_custom_field_settings_bundles_enum_id_delete) | **DELETE** /admin/customFieldSettings/bundles/enum/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_enum_id_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_enum_id_get) | **GET** /admin/customFieldSettings/bundles/enum/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_enum_id_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_enum_id_post) | **POST** /admin/customFieldSettings/bundles/enum/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_enum_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_enum_post) | **POST** /admin/customFieldSettings/bundles/enum | 
*DefaultApi* | [**admin_custom_field_settings_bundles_owned_field_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_owned_field_get) | **GET** /admin/customFieldSettings/bundles/ownedField | 
*DefaultApi* | [**admin_custom_field_settings_bundles_owned_field_id_delete**](docs/DefaultApi.md#admin_custom_field_settings_bundles_owned_field_id_delete) | **DELETE** /admin/customFieldSettings/bundles/ownedField/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_owned_field_id_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_owned_field_id_get) | **GET** /admin/customFieldSettings/bundles/ownedField/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_owned_field_id_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_owned_field_id_post) | **POST** /admin/customFieldSettings/bundles/ownedField/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_owned_field_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_owned_field_post) | **POST** /admin/customFieldSettings/bundles/ownedField | 
*DefaultApi* | [**admin_custom_field_settings_bundles_state_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_state_get) | **GET** /admin/customFieldSettings/bundles/state | 
*DefaultApi* | [**admin_custom_field_settings_bundles_state_id_delete**](docs/DefaultApi.md#admin_custom_field_settings_bundles_state_id_delete) | **DELETE** /admin/customFieldSettings/bundles/state/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_state_id_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_state_id_get) | **GET** /admin/customFieldSettings/bundles/state/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_state_id_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_state_id_post) | **POST** /admin/customFieldSettings/bundles/state/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_state_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_state_post) | **POST** /admin/customFieldSettings/bundles/state | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_get) | **GET** /admin/customFieldSettings/bundles/user | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_id_aggregated_users_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_id_aggregated_users_get) | **GET** /admin/customFieldSettings/bundles/user/{id}/aggregatedUsers | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_id_delete**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_id_delete) | **DELETE** /admin/customFieldSettings/bundles/user/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_id_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_id_get) | **GET** /admin/customFieldSettings/bundles/user/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_id_groups_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_id_groups_get) | **GET** /admin/customFieldSettings/bundles/user/{id}/groups | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_id_groups_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_id_groups_post) | **POST** /admin/customFieldSettings/bundles/user/{id}/groups | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_id_groups_user_group_id_delete**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_id_groups_user_group_id_delete) | **DELETE** /admin/customFieldSettings/bundles/user/{id}/groups/{userGroupId} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_id_groups_user_group_id_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_id_groups_user_group_id_get) | **GET** /admin/customFieldSettings/bundles/user/{id}/groups/{userGroupId} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_id_individuals_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_id_individuals_get) | **GET** /admin/customFieldSettings/bundles/user/{id}/individuals | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_id_individuals_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_id_individuals_post) | **POST** /admin/customFieldSettings/bundles/user/{id}/individuals | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_id_individuals_user_id_delete**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_id_individuals_user_id_delete) | **DELETE** /admin/customFieldSettings/bundles/user/{id}/individuals/{userId} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_id_individuals_user_id_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_id_individuals_user_id_get) | **GET** /admin/customFieldSettings/bundles/user/{id}/individuals/{userId} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_id_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_id_post) | **POST** /admin/customFieldSettings/bundles/user/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_user_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_user_post) | **POST** /admin/customFieldSettings/bundles/user | 
*DefaultApi* | [**admin_custom_field_settings_bundles_version_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_version_get) | **GET** /admin/customFieldSettings/bundles/version | 
*DefaultApi* | [**admin_custom_field_settings_bundles_version_id_delete**](docs/DefaultApi.md#admin_custom_field_settings_bundles_version_id_delete) | **DELETE** /admin/customFieldSettings/bundles/version/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_version_id_get**](docs/DefaultApi.md#admin_custom_field_settings_bundles_version_id_get) | **GET** /admin/customFieldSettings/bundles/version/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_version_id_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_version_id_post) | **POST** /admin/customFieldSettings/bundles/version/{id} | 
*DefaultApi* | [**admin_custom_field_settings_bundles_version_post**](docs/DefaultApi.md#admin_custom_field_settings_bundles_version_post) | **POST** /admin/customFieldSettings/bundles/version | 
*DefaultApi* | [**admin_custom_field_settings_custom_fields_get**](docs/DefaultApi.md#admin_custom_field_settings_custom_fields_get) | **GET** /admin/customFieldSettings/customFields | 
*DefaultApi* | [**admin_custom_field_settings_custom_fields_id_delete**](docs/DefaultApi.md#admin_custom_field_settings_custom_fields_id_delete) | **DELETE** /admin/customFieldSettings/customFields/{id} | 
*DefaultApi* | [**admin_custom_field_settings_custom_fields_id_field_defaults_get**](docs/DefaultApi.md#admin_custom_field_settings_custom_fields_id_field_defaults_get) | **GET** /admin/customFieldSettings/customFields/{id}/fieldDefaults | 
*DefaultApi* | [**admin_custom_field_settings_custom_fields_id_field_defaults_post**](docs/DefaultApi.md#admin_custom_field_settings_custom_fields_id_field_defaults_post) | **POST** /admin/customFieldSettings/customFields/{id}/fieldDefaults | 
*DefaultApi* | [**admin_custom_field_settings_custom_fields_id_get**](docs/DefaultApi.md#admin_custom_field_settings_custom_fields_id_get) | **GET** /admin/customFieldSettings/customFields/{id} | 
*DefaultApi* | [**admin_custom_field_settings_custom_fields_id_instances_get**](docs/DefaultApi.md#admin_custom_field_settings_custom_fields_id_instances_get) | **GET** /admin/customFieldSettings/customFields/{id}/instances | 
*DefaultApi* | [**admin_custom_field_settings_custom_fields_id_post**](docs/DefaultApi.md#admin_custom_field_settings_custom_fields_id_post) | **POST** /admin/customFieldSettings/customFields/{id} | 
*DefaultApi* | [**admin_custom_field_settings_custom_fields_post**](docs/DefaultApi.md#admin_custom_field_settings_custom_fields_post) | **POST** /admin/customFieldSettings/customFields | 
*DefaultApi* | [**admin_custom_field_settings_types_get**](docs/DefaultApi.md#admin_custom_field_settings_types_get) | **GET** /admin/customFieldSettings/types | 
*DefaultApi* | [**admin_database_backup_backups_get**](docs/DefaultApi.md#admin_database_backup_backups_get) | **GET** /admin/databaseBackup/backups | 
*DefaultApi* | [**admin_database_backup_backups_id_get**](docs/DefaultApi.md#admin_database_backup_backups_id_get) | **GET** /admin/databaseBackup/backups/{id} | 
*DefaultApi* | [**admin_database_backup_settings_backup_status_get**](docs/DefaultApi.md#admin_database_backup_settings_backup_status_get) | **GET** /admin/databaseBackup/settings/backupStatus | 
*DefaultApi* | [**admin_database_backup_settings_get**](docs/DefaultApi.md#admin_database_backup_settings_get) | **GET** /admin/databaseBackup/settings | 
*DefaultApi* | [**admin_database_backup_settings_post**](docs/DefaultApi.md#admin_database_backup_settings_post) | **POST** /admin/databaseBackup/settings | 
*DefaultApi* | [**admin_global_settings_appearance_settings_get**](docs/DefaultApi.md#admin_global_settings_appearance_settings_get) | **GET** /admin/globalSettings/appearanceSettings | 
*DefaultApi* | [**admin_global_settings_appearance_settings_post**](docs/DefaultApi.md#admin_global_settings_appearance_settings_post) | **POST** /admin/globalSettings/appearanceSettings | 
*DefaultApi* | [**admin_global_settings_get**](docs/DefaultApi.md#admin_global_settings_get) | **GET** /admin/globalSettings | 
*DefaultApi* | [**admin_global_settings_license_get**](docs/DefaultApi.md#admin_global_settings_license_get) | **GET** /admin/globalSettings/license | 
*DefaultApi* | [**admin_global_settings_license_post**](docs/DefaultApi.md#admin_global_settings_license_post) | **POST** /admin/globalSettings/license | 
*DefaultApi* | [**admin_global_settings_locale_settings_get**](docs/DefaultApi.md#admin_global_settings_locale_settings_get) | **GET** /admin/globalSettings/localeSettings | 
*DefaultApi* | [**admin_global_settings_locale_settings_post**](docs/DefaultApi.md#admin_global_settings_locale_settings_post) | **POST** /admin/globalSettings/localeSettings | 
*DefaultApi* | [**admin_global_settings_notification_settings_get**](docs/DefaultApi.md#admin_global_settings_notification_settings_get) | **GET** /admin/globalSettings/notificationSettings | 
*DefaultApi* | [**admin_global_settings_notification_settings_post**](docs/DefaultApi.md#admin_global_settings_notification_settings_post) | **POST** /admin/globalSettings/notificationSettings | 
*DefaultApi* | [**admin_global_settings_post**](docs/DefaultApi.md#admin_global_settings_post) | **POST** /admin/globalSettings | 
*DefaultApi* | [**admin_global_settings_rest_settings_get**](docs/DefaultApi.md#admin_global_settings_rest_settings_get) | **GET** /admin/globalSettings/restSettings | 
*DefaultApi* | [**admin_global_settings_rest_settings_post**](docs/DefaultApi.md#admin_global_settings_rest_settings_post) | **POST** /admin/globalSettings/restSettings | 
*DefaultApi* | [**admin_global_settings_system_settings_get**](docs/DefaultApi.md#admin_global_settings_system_settings_get) | **GET** /admin/globalSettings/systemSettings | 
*DefaultApi* | [**admin_global_settings_system_settings_post**](docs/DefaultApi.md#admin_global_settings_system_settings_post) | **POST** /admin/globalSettings/systemSettings | 
*DefaultApi* | [**admin_projects_get**](docs/DefaultApi.md#admin_projects_get) | **GET** /admin/projects | 
*DefaultApi* | [**admin_projects_id_custom_fields_get**](docs/DefaultApi.md#admin_projects_id_custom_fields_get) | **GET** /admin/projects/{id}/customFields | 
*DefaultApi* | [**admin_projects_id_custom_fields_post**](docs/DefaultApi.md#admin_projects_id_custom_fields_post) | **POST** /admin/projects/{id}/customFields | 
*DefaultApi* | [**admin_projects_id_custom_fields_project_custom_field_id_delete**](docs/DefaultApi.md#admin_projects_id_custom_fields_project_custom_field_id_delete) | **DELETE** /admin/projects/{id}/customFields/{projectCustomFieldId} | 
*DefaultApi* | [**admin_projects_id_custom_fields_project_custom_field_id_get**](docs/DefaultApi.md#admin_projects_id_custom_fields_project_custom_field_id_get) | **GET** /admin/projects/{id}/customFields/{projectCustomFieldId} | 
*DefaultApi* | [**admin_projects_id_custom_fields_project_custom_field_id_post**](docs/DefaultApi.md#admin_projects_id_custom_fields_project_custom_field_id_post) | **POST** /admin/projects/{id}/customFields/{projectCustomFieldId} | 
*DefaultApi* | [**admin_projects_id_delete**](docs/DefaultApi.md#admin_projects_id_delete) | **DELETE** /admin/projects/{id} | 
*DefaultApi* | [**admin_projects_id_get**](docs/DefaultApi.md#admin_projects_id_get) | **GET** /admin/projects/{id} | 
*DefaultApi* | [**admin_projects_id_issues_get**](docs/DefaultApi.md#admin_projects_id_issues_get) | **GET** /admin/projects/{id}/issues | 
*DefaultApi* | [**admin_projects_id_issues_issue_id_delete**](docs/DefaultApi.md#admin_projects_id_issues_issue_id_delete) | **DELETE** /admin/projects/{id}/issues/{issueId} | 
*DefaultApi* | [**admin_projects_id_issues_issue_id_get**](docs/DefaultApi.md#admin_projects_id_issues_issue_id_get) | **GET** /admin/projects/{id}/issues/{issueId} | 
*DefaultApi* | [**admin_projects_id_issues_issue_id_post**](docs/DefaultApi.md#admin_projects_id_issues_issue_id_post) | **POST** /admin/projects/{id}/issues/{issueId} | 
*DefaultApi* | [**admin_projects_id_issues_post**](docs/DefaultApi.md#admin_projects_id_issues_post) | **POST** /admin/projects/{id}/issues | 
*DefaultApi* | [**admin_projects_id_post**](docs/DefaultApi.md#admin_projects_id_post) | **POST** /admin/projects/{id} | 
*DefaultApi* | [**admin_projects_id_time_tracking_settings_get**](docs/DefaultApi.md#admin_projects_id_time_tracking_settings_get) | **GET** /admin/projects/{id}/timeTrackingSettings | 
*DefaultApi* | [**admin_projects_id_time_tracking_settings_post**](docs/DefaultApi.md#admin_projects_id_time_tracking_settings_post) | **POST** /admin/projects/{id}/timeTrackingSettings | 
*DefaultApi* | [**admin_projects_id_time_tracking_settings_work_item_types_get**](docs/DefaultApi.md#admin_projects_id_time_tracking_settings_work_item_types_get) | **GET** /admin/projects/{id}/timeTrackingSettings/workItemTypes | 
*DefaultApi* | [**admin_projects_id_time_tracking_settings_work_item_types_post**](docs/DefaultApi.md#admin_projects_id_time_tracking_settings_work_item_types_post) | **POST** /admin/projects/{id}/timeTrackingSettings/workItemTypes | 
*DefaultApi* | [**admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_delete**](docs/DefaultApi.md#admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_delete) | **DELETE** /admin/projects/{id}/timeTrackingSettings/workItemTypes/{workItemTypeId} | 
*DefaultApi* | [**admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_get**](docs/DefaultApi.md#admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_get) | **GET** /admin/projects/{id}/timeTrackingSettings/workItemTypes/{workItemTypeId} | 
*DefaultApi* | [**admin_projects_post**](docs/DefaultApi.md#admin_projects_post) | **POST** /admin/projects | 
*DefaultApi* | [**admin_telemetry_get**](docs/DefaultApi.md#admin_telemetry_get) | **GET** /admin/telemetry | 
*DefaultApi* | [**admin_time_tracking_settings_get**](docs/DefaultApi.md#admin_time_tracking_settings_get) | **GET** /admin/timeTrackingSettings | 
*DefaultApi* | [**admin_time_tracking_settings_work_item_types_get**](docs/DefaultApi.md#admin_time_tracking_settings_work_item_types_get) | **GET** /admin/timeTrackingSettings/workItemTypes | 
*DefaultApi* | [**admin_time_tracking_settings_work_item_types_post**](docs/DefaultApi.md#admin_time_tracking_settings_work_item_types_post) | **POST** /admin/timeTrackingSettings/workItemTypes | 
*DefaultApi* | [**admin_time_tracking_settings_work_item_types_work_item_type_id_delete**](docs/DefaultApi.md#admin_time_tracking_settings_work_item_types_work_item_type_id_delete) | **DELETE** /admin/timeTrackingSettings/workItemTypes/{workItemTypeId} | 
*DefaultApi* | [**admin_time_tracking_settings_work_item_types_work_item_type_id_get**](docs/DefaultApi.md#admin_time_tracking_settings_work_item_types_work_item_type_id_get) | **GET** /admin/timeTrackingSettings/workItemTypes/{workItemTypeId} | 
*DefaultApi* | [**admin_time_tracking_settings_work_item_types_work_item_type_id_post**](docs/DefaultApi.md#admin_time_tracking_settings_work_item_types_work_item_type_id_post) | **POST** /admin/timeTrackingSettings/workItemTypes/{workItemTypeId} | 
*DefaultApi* | [**admin_time_tracking_settings_work_time_settings_get**](docs/DefaultApi.md#admin_time_tracking_settings_work_time_settings_get) | **GET** /admin/timeTrackingSettings/workTimeSettings | 
*DefaultApi* | [**admin_time_tracking_settings_work_time_settings_post**](docs/DefaultApi.md#admin_time_tracking_settings_work_time_settings_post) | **POST** /admin/timeTrackingSettings/workTimeSettings | 
*DefaultApi* | [**agiles_get**](docs/DefaultApi.md#agiles_get) | **GET** /agiles | 
*DefaultApi* | [**agiles_id_delete**](docs/DefaultApi.md#agiles_id_delete) | **DELETE** /agiles/{id} | 
*DefaultApi* | [**agiles_id_get**](docs/DefaultApi.md#agiles_id_get) | **GET** /agiles/{id} | 
*DefaultApi* | [**agiles_id_post**](docs/DefaultApi.md#agiles_id_post) | **POST** /agiles/{id} | 
*DefaultApi* | [**agiles_id_sprints_get**](docs/DefaultApi.md#agiles_id_sprints_get) | **GET** /agiles/{id}/sprints | 
*DefaultApi* | [**agiles_id_sprints_post**](docs/DefaultApi.md#agiles_id_sprints_post) | **POST** /agiles/{id}/sprints | 
*DefaultApi* | [**agiles_id_sprints_sprint_id_delete**](docs/DefaultApi.md#agiles_id_sprints_sprint_id_delete) | **DELETE** /agiles/{id}/sprints/{sprintId} | 
*DefaultApi* | [**agiles_id_sprints_sprint_id_get**](docs/DefaultApi.md#agiles_id_sprints_sprint_id_get) | **GET** /agiles/{id}/sprints/{sprintId} | 
*DefaultApi* | [**agiles_id_sprints_sprint_id_post**](docs/DefaultApi.md#agiles_id_sprints_sprint_id_post) | **POST** /agiles/{id}/sprints/{sprintId} | 
*DefaultApi* | [**agiles_post**](docs/DefaultApi.md#agiles_post) | **POST** /agiles | 
*DefaultApi* | [**groups_get**](docs/DefaultApi.md#groups_get) | **GET** /groups | 
*DefaultApi* | [**groups_id_get**](docs/DefaultApi.md#groups_id_get) | **GET** /groups/{id} | 
*DefaultApi* | [**issue_link_types_get**](docs/DefaultApi.md#issue_link_types_get) | **GET** /issueLinkTypes | 
*DefaultApi* | [**issue_link_types_id_delete**](docs/DefaultApi.md#issue_link_types_id_delete) | **DELETE** /issueLinkTypes/{id} | 
*DefaultApi* | [**issue_link_types_id_get**](docs/DefaultApi.md#issue_link_types_id_get) | **GET** /issueLinkTypes/{id} | 
*DefaultApi* | [**issue_link_types_id_post**](docs/DefaultApi.md#issue_link_types_id_post) | **POST** /issueLinkTypes/{id} | 
*DefaultApi* | [**issue_link_types_post**](docs/DefaultApi.md#issue_link_types_post) | **POST** /issueLinkTypes | 
*DefaultApi* | [**issue_tags_get**](docs/DefaultApi.md#issue_tags_get) | **GET** /issueTags | 
*DefaultApi* | [**issue_tags_id_delete**](docs/DefaultApi.md#issue_tags_id_delete) | **DELETE** /issueTags/{id} | 
*DefaultApi* | [**issue_tags_id_get**](docs/DefaultApi.md#issue_tags_id_get) | **GET** /issueTags/{id} | 
*DefaultApi* | [**issue_tags_id_issues_get**](docs/DefaultApi.md#issue_tags_id_issues_get) | **GET** /issueTags/{id}/issues | 
*DefaultApi* | [**issue_tags_id_post**](docs/DefaultApi.md#issue_tags_id_post) | **POST** /issueTags/{id} | 
*DefaultApi* | [**issue_tags_post**](docs/DefaultApi.md#issue_tags_post) | **POST** /issueTags | 
*DefaultApi* | [**issues_get**](docs/DefaultApi.md#issues_get) | **GET** /issues | 
*DefaultApi* | [**issues_id_activities_activity_item_id_get**](docs/DefaultApi.md#issues_id_activities_activity_item_id_get) | **GET** /issues/{id}/activities/{activityItemId} | 
*DefaultApi* | [**issues_id_activities_get**](docs/DefaultApi.md#issues_id_activities_get) | **GET** /issues/{id}/activities | 
*DefaultApi* | [**issues_id_activities_page_get**](docs/DefaultApi.md#issues_id_activities_page_get) | **GET** /issues/{id}/activitiesPage | 
*DefaultApi* | [**issues_id_attachments_get**](docs/DefaultApi.md#issues_id_attachments_get) | **GET** /issues/{id}/attachments | 
*DefaultApi* | [**issues_id_attachments_issue_attachment_id_delete**](docs/DefaultApi.md#issues_id_attachments_issue_attachment_id_delete) | **DELETE** /issues/{id}/attachments/{issueAttachmentId} | 
*DefaultApi* | [**issues_id_attachments_issue_attachment_id_get**](docs/DefaultApi.md#issues_id_attachments_issue_attachment_id_get) | **GET** /issues/{id}/attachments/{issueAttachmentId} | 
*DefaultApi* | [**issues_id_attachments_issue_attachment_id_post**](docs/DefaultApi.md#issues_id_attachments_issue_attachment_id_post) | **POST** /issues/{id}/attachments/{issueAttachmentId} | 
*DefaultApi* | [**issues_id_attachments_post**](docs/DefaultApi.md#issues_id_attachments_post) | **POST** /issues/{id}/attachments | 
*DefaultApi* | [**issues_id_comments_get**](docs/DefaultApi.md#issues_id_comments_get) | **GET** /issues/{id}/comments | 
*DefaultApi* | [**issues_id_comments_issue_comment_id_delete**](docs/DefaultApi.md#issues_id_comments_issue_comment_id_delete) | **DELETE** /issues/{id}/comments/{issueCommentId} | 
*DefaultApi* | [**issues_id_comments_issue_comment_id_get**](docs/DefaultApi.md#issues_id_comments_issue_comment_id_get) | **GET** /issues/{id}/comments/{issueCommentId} | 
*DefaultApi* | [**issues_id_comments_issue_comment_id_post**](docs/DefaultApi.md#issues_id_comments_issue_comment_id_post) | **POST** /issues/{id}/comments/{issueCommentId} | 
*DefaultApi* | [**issues_id_comments_post**](docs/DefaultApi.md#issues_id_comments_post) | **POST** /issues/{id}/comments | 
*DefaultApi* | [**issues_id_custom_fields_get**](docs/DefaultApi.md#issues_id_custom_fields_get) | **GET** /issues/{id}/customFields | 
*DefaultApi* | [**issues_id_custom_fields_issue_custom_field_id_get**](docs/DefaultApi.md#issues_id_custom_fields_issue_custom_field_id_get) | **GET** /issues/{id}/customFields/{issueCustomFieldId} | 
*DefaultApi* | [**issues_id_custom_fields_issue_custom_field_id_post**](docs/DefaultApi.md#issues_id_custom_fields_issue_custom_field_id_post) | **POST** /issues/{id}/customFields/{issueCustomFieldId} | 
*DefaultApi* | [**issues_id_delete**](docs/DefaultApi.md#issues_id_delete) | **DELETE** /issues/{id} | 
*DefaultApi* | [**issues_id_get**](docs/DefaultApi.md#issues_id_get) | **GET** /issues/{id} | 
*DefaultApi* | [**issues_id_links_get**](docs/DefaultApi.md#issues_id_links_get) | **GET** /issues/{id}/links | 
*DefaultApi* | [**issues_id_links_issue_link_id_get**](docs/DefaultApi.md#issues_id_links_issue_link_id_get) | **GET** /issues/{id}/links/{issueLinkId} | 
*DefaultApi* | [**issues_id_links_issue_link_id_issues_get**](docs/DefaultApi.md#issues_id_links_issue_link_id_issues_get) | **GET** /issues/{id}/links/{issueLinkId}/issues | 
*DefaultApi* | [**issues_id_links_issue_link_id_issues_issue_id_delete**](docs/DefaultApi.md#issues_id_links_issue_link_id_issues_issue_id_delete) | **DELETE** /issues/{id}/links/{issueLinkId}/issues/{issueId} | 
*DefaultApi* | [**issues_id_links_issue_link_id_issues_post**](docs/DefaultApi.md#issues_id_links_issue_link_id_issues_post) | **POST** /issues/{id}/links/{issueLinkId}/issues | 
*DefaultApi* | [**issues_id_post**](docs/DefaultApi.md#issues_id_post) | **POST** /issues/{id} | 
*DefaultApi* | [**issues_id_project_get**](docs/DefaultApi.md#issues_id_project_get) | **GET** /issues/{id}/project | 
*DefaultApi* | [**issues_id_project_post**](docs/DefaultApi.md#issues_id_project_post) | **POST** /issues/{id}/project | 
*DefaultApi* | [**issues_id_time_tracking_get**](docs/DefaultApi.md#issues_id_time_tracking_get) | **GET** /issues/{id}/timeTracking | 
*DefaultApi* | [**issues_id_time_tracking_work_items_get**](docs/DefaultApi.md#issues_id_time_tracking_work_items_get) | **GET** /issues/{id}/timeTracking/workItems | 
*DefaultApi* | [**issues_id_time_tracking_work_items_issue_work_item_id_delete**](docs/DefaultApi.md#issues_id_time_tracking_work_items_issue_work_item_id_delete) | **DELETE** /issues/{id}/timeTracking/workItems/{issueWorkItemId} | 
*DefaultApi* | [**issues_id_time_tracking_work_items_issue_work_item_id_get**](docs/DefaultApi.md#issues_id_time_tracking_work_items_issue_work_item_id_get) | **GET** /issues/{id}/timeTracking/workItems/{issueWorkItemId} | 
*DefaultApi* | [**issues_id_time_tracking_work_items_issue_work_item_id_post**](docs/DefaultApi.md#issues_id_time_tracking_work_items_issue_work_item_id_post) | **POST** /issues/{id}/timeTracking/workItems/{issueWorkItemId} | 
*DefaultApi* | [**issues_id_time_tracking_work_items_post**](docs/DefaultApi.md#issues_id_time_tracking_work_items_post) | **POST** /issues/{id}/timeTracking/workItems | 
*DefaultApi* | [**issues_post**](docs/DefaultApi.md#issues_post) | **POST** /issues | 
*DefaultApi* | [**saved_queries_get**](docs/DefaultApi.md#saved_queries_get) | **GET** /savedQueries | 
*DefaultApi* | [**saved_queries_id_delete**](docs/DefaultApi.md#saved_queries_id_delete) | **DELETE** /savedQueries/{id} | 
*DefaultApi* | [**saved_queries_id_get**](docs/DefaultApi.md#saved_queries_id_get) | **GET** /savedQueries/{id} | 
*DefaultApi* | [**saved_queries_id_post**](docs/DefaultApi.md#saved_queries_id_post) | **POST** /savedQueries/{id} | 
*DefaultApi* | [**saved_queries_post**](docs/DefaultApi.md#saved_queries_post) | **POST** /savedQueries | 
*DefaultApi* | [**users_get**](docs/DefaultApi.md#users_get) | **GET** /users | 
*DefaultApi* | [**users_id_get**](docs/DefaultApi.md#users_id_get) | **GET** /users/{id} | 
*DefaultApi* | [**users_id_profiles_general_get**](docs/DefaultApi.md#users_id_profiles_general_get) | **GET** /users/{id}/profiles/general | 
*DefaultApi* | [**users_id_profiles_general_post**](docs/DefaultApi.md#users_id_profiles_general_post) | **POST** /users/{id}/profiles/general | 
*DefaultApi* | [**users_id_profiles_notifications_get**](docs/DefaultApi.md#users_id_profiles_notifications_get) | **GET** /users/{id}/profiles/notifications | 
*DefaultApi* | [**users_id_profiles_notifications_post**](docs/DefaultApi.md#users_id_profiles_notifications_post) | **POST** /users/{id}/profiles/notifications | 
*DefaultApi* | [**users_id_profiles_timetracking_get**](docs/DefaultApi.md#users_id_profiles_timetracking_get) | **GET** /users/{id}/profiles/timetracking | 
*DefaultApi* | [**users_id_profiles_timetracking_post**](docs/DefaultApi.md#users_id_profiles_timetracking_post) | **POST** /users/{id}/profiles/timetracking | 
*DefaultApi* | [**users_id_saved_queries_get**](docs/DefaultApi.md#users_id_saved_queries_get) | **GET** /users/{id}/savedQueries | 
*DefaultApi* | [**users_id_tags_get**](docs/DefaultApi.md#users_id_tags_get) | **GET** /users/{id}/tags | 
*DefaultApi* | [**users_me_get**](docs/DefaultApi.md#users_me_get) | **GET** /users/me | 
*DefaultApi* | [**work_items_get**](docs/DefaultApi.md#work_items_get) | **GET** /workItems | 
*DefaultApi* | [**work_items_id_get**](docs/DefaultApi.md#work_items_id_get) | **GET** /workItems/{id} | 


## Documentation For Models



## Documentation For Authorization


## permanentToken

- **Type**: Bearer authentication (YouTrack permanent token)


## Author




