# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable, List

from fastapi.encoders import jsonable_encoder

from yt_client import models as m

if TYPE_CHECKING:
    from yt_client.api_client import ApiClient


class _DefaultApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_activities_get(
        self,
        categories: str = None,
        reverse: bool = None,
        start: str = None,
        end: str = None,
        author: str = None,
        issue_query: str = None,
        fields: str = None,
        skip: int = None,
        top: int = None,
    ) -> Awaitable[List[m.ActivityItem]]:
        query_params = {}
        if categories is not None:
            query_params["categories"] = str(categories)
        if reverse is not None:
            query_params["reverse"] = str(reverse)
        if start is not None:
            query_params["start"] = str(start)
        if end is not None:
            query_params["end"] = str(end)
        if author is not None:
            query_params["author"] = str(author)
        if issue_query is not None:
            query_params["issueQuery"] = str(issue_query)
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.ActivityItem],
            method="GET",
            url="/activities",
            params=query_params,
        )

    def _build_for_activities_id_get(self, id: str, fields: str = None) -> Awaitable[m.ActivityItem]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.ActivityItem,
            method="GET",
            url="/activities/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_activities_page_get(
        self,
        categories: str = None,
        reverse: bool = None,
        start: str = None,
        end: str = None,
        author: str = None,
        issue_query: str = None,
        cursor: str = None,
        activity_id: str = None,
        fields: str = None,
    ) -> Awaitable[m.ActivityCursorPage]:
        query_params = {}
        if categories is not None:
            query_params["categories"] = str(categories)
        if reverse is not None:
            query_params["reverse"] = str(reverse)
        if start is not None:
            query_params["start"] = str(start)
        if end is not None:
            query_params["end"] = str(end)
        if author is not None:
            query_params["author"] = str(author)
        if issue_query is not None:
            query_params["issueQuery"] = str(issue_query)
        if cursor is not None:
            query_params["cursor"] = str(cursor)
        if activity_id is not None:
            query_params["activityId"] = str(activity_id)
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.ActivityCursorPage,
            method="GET",
            url="/activitiesPage",
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_build_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.BuildBundle]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.BuildBundle],
            method="GET",
            url="/admin/customFieldSettings/bundles/build",
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_build_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/customFieldSettings/bundles/build/{id}",
            path_params=path_params,
        )

    def _build_for_admin_custom_field_settings_bundles_build_id_get(
        self, id: str, fields: str = None
    ) -> Awaitable[m.BuildBundle]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.BuildBundle,
            method="GET",
            url="/admin/customFieldSettings/bundles/build/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_build_id_post(
        self, id: str, fields: str = None, build_bundle: m.BuildBundle = None
    ) -> Awaitable[m.BuildBundle]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(build_bundle)

        return self.api_client.request(
            type_=m.BuildBundle,
            method="POST",
            url="/admin/customFieldSettings/bundles/build/{id}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_build_post(
        self, fields: str = None, build_bundle: m.BuildBundle = None
    ) -> Awaitable[m.BuildBundle]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(build_bundle)

        return self.api_client.request(
            type_=m.BuildBundle,
            method="POST",
            url="/admin/customFieldSettings/bundles/build",
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_enum_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.EnumBundle]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.EnumBundle],
            method="GET",
            url="/admin/customFieldSettings/bundles/enum",
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_enum_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/customFieldSettings/bundles/enum/{id}",
            path_params=path_params,
        )

    def _build_for_admin_custom_field_settings_bundles_enum_id_get(
        self, id: str, fields: str = None
    ) -> Awaitable[m.EnumBundle]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.EnumBundle,
            method="GET",
            url="/admin/customFieldSettings/bundles/enum/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_enum_id_post(
        self, id: str, fields: str = None, enum_bundle: m.EnumBundle = None
    ) -> Awaitable[m.EnumBundle]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(enum_bundle)

        return self.api_client.request(
            type_=m.EnumBundle,
            method="POST",
            url="/admin/customFieldSettings/bundles/enum/{id}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_enum_post(
        self, fields: str = None, enum_bundle: m.EnumBundle = None
    ) -> Awaitable[m.EnumBundle]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(enum_bundle)

        return self.api_client.request(
            type_=m.EnumBundle,
            method="POST",
            url="/admin/customFieldSettings/bundles/enum",
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_owned_field_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.OwnedBundle]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.OwnedBundle],
            method="GET",
            url="/admin/customFieldSettings/bundles/ownedField",
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_owned_field_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/customFieldSettings/bundles/ownedField/{id}",
            path_params=path_params,
        )

    def _build_for_admin_custom_field_settings_bundles_owned_field_id_get(
        self, id: str, fields: str = None
    ) -> Awaitable[m.OwnedBundle]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.OwnedBundle,
            method="GET",
            url="/admin/customFieldSettings/bundles/ownedField/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_owned_field_id_post(
        self, id: str, fields: str = None, owned_bundle: m.OwnedBundle = None
    ) -> Awaitable[m.OwnedBundle]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(owned_bundle)

        return self.api_client.request(
            type_=m.OwnedBundle,
            method="POST",
            url="/admin/customFieldSettings/bundles/ownedField/{id}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_owned_field_post(
        self, fields: str = None, owned_bundle: m.OwnedBundle = None
    ) -> Awaitable[m.OwnedBundle]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(owned_bundle)

        return self.api_client.request(
            type_=m.OwnedBundle,
            method="POST",
            url="/admin/customFieldSettings/bundles/ownedField",
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_state_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.StateBundle]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.StateBundle],
            method="GET",
            url="/admin/customFieldSettings/bundles/state",
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_state_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/customFieldSettings/bundles/state/{id}",
            path_params=path_params,
        )

    def _build_for_admin_custom_field_settings_bundles_state_id_get(
        self, id: str, fields: str = None
    ) -> Awaitable[m.StateBundle]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.StateBundle,
            method="GET",
            url="/admin/customFieldSettings/bundles/state/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_state_id_post(
        self, id: str, fields: str = None, state_bundle: m.StateBundle = None
    ) -> Awaitable[m.StateBundle]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(state_bundle)

        return self.api_client.request(
            type_=m.StateBundle,
            method="POST",
            url="/admin/customFieldSettings/bundles/state/{id}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_state_post(
        self, fields: str = None, state_bundle: m.StateBundle = None
    ) -> Awaitable[m.StateBundle]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(state_bundle)

        return self.api_client.request(
            type_=m.StateBundle,
            method="POST",
            url="/admin/customFieldSettings/bundles/state",
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_user_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.UserBundle]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.UserBundle],
            method="GET",
            url="/admin/customFieldSettings/bundles/user",
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_user_id_aggregated_users_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.User]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.User],
            method="GET",
            url="/admin/customFieldSettings/bundles/user/{id}/aggregatedUsers",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_user_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/customFieldSettings/bundles/user/{id}",
            path_params=path_params,
        )

    def _build_for_admin_custom_field_settings_bundles_user_id_get(
        self, id: str, fields: str = None
    ) -> Awaitable[m.UserBundle]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.UserBundle,
            method="GET",
            url="/admin/customFieldSettings/bundles/user/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_user_id_groups_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.UserGroup]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.UserGroup],
            method="GET",
            url="/admin/customFieldSettings/bundles/user/{id}/groups",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_user_id_groups_post(
        self, id: str, fields: str = None, user_group: m.UserGroup = None
    ) -> Awaitable[m.UserGroup]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(user_group)

        return self.api_client.request(
            type_=m.UserGroup,
            method="POST",
            url="/admin/customFieldSettings/bundles/user/{id}/groups",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_user_id_groups_user_group_id_delete(
        self, id: str, user_group_id: str
    ) -> Awaitable[None]:
        path_params = {"id": str(id), "userGroupId": str(user_group_id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/customFieldSettings/bundles/user/{id}/groups/{userGroupId}",
            path_params=path_params,
        )

    def _build_for_admin_custom_field_settings_bundles_user_id_groups_user_group_id_get(
        self, id: str, user_group_id: str, fields: str = None
    ) -> Awaitable[m.UserGroup]:
        path_params = {"id": str(id), "userGroupId": str(user_group_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.UserGroup,
            method="GET",
            url="/admin/customFieldSettings/bundles/user/{id}/groups/{userGroupId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_user_id_individuals_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.User]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.User],
            method="GET",
            url="/admin/customFieldSettings/bundles/user/{id}/individuals",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_user_id_individuals_post(
        self, id: str, fields: str = None, user: m.User = None
    ) -> Awaitable[m.User]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(user)

        return self.api_client.request(
            type_=m.User,
            method="POST",
            url="/admin/customFieldSettings/bundles/user/{id}/individuals",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_user_id_individuals_user_id_delete(
        self, id: str, user_id: str
    ) -> Awaitable[None]:
        path_params = {"id": str(id), "userId": str(user_id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/customFieldSettings/bundles/user/{id}/individuals/{userId}",
            path_params=path_params,
        )

    def _build_for_admin_custom_field_settings_bundles_user_id_individuals_user_id_get(
        self, id: str, user_id: str, fields: str = None
    ) -> Awaitable[m.User]:
        path_params = {"id": str(id), "userId": str(user_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.User,
            method="GET",
            url="/admin/customFieldSettings/bundles/user/{id}/individuals/{userId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_user_id_post(
        self, id: str, fields: str = None, user_bundle: m.UserBundle = None
    ) -> Awaitable[m.UserBundle]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(user_bundle)

        return self.api_client.request(
            type_=m.UserBundle,
            method="POST",
            url="/admin/customFieldSettings/bundles/user/{id}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_user_post(
        self, fields: str = None, user_bundle: m.UserBundle = None
    ) -> Awaitable[m.UserBundle]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(user_bundle)

        return self.api_client.request(
            type_=m.UserBundle,
            method="POST",
            url="/admin/customFieldSettings/bundles/user",
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_version_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.VersionBundle]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.VersionBundle],
            method="GET",
            url="/admin/customFieldSettings/bundles/version",
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_version_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/customFieldSettings/bundles/version/{id}",
            path_params=path_params,
        )

    def _build_for_admin_custom_field_settings_bundles_version_id_get(
        self, id: str, fields: str = None
    ) -> Awaitable[m.VersionBundle]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.VersionBundle,
            method="GET",
            url="/admin/customFieldSettings/bundles/version/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_bundles_version_id_post(
        self, id: str, fields: str = None, version_bundle: m.VersionBundle = None
    ) -> Awaitable[m.VersionBundle]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(version_bundle)

        return self.api_client.request(
            type_=m.VersionBundle,
            method="POST",
            url="/admin/customFieldSettings/bundles/version/{id}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_bundles_version_post(
        self, fields: str = None, version_bundle: m.VersionBundle = None
    ) -> Awaitable[m.VersionBundle]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(version_bundle)

        return self.api_client.request(
            type_=m.VersionBundle,
            method="POST",
            url="/admin/customFieldSettings/bundles/version",
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_custom_fields_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.CustomField]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.CustomField],
            method="GET",
            url="/admin/customFieldSettings/customFields",
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_custom_fields_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/customFieldSettings/customFields/{id}",
            path_params=path_params,
        )

    def _build_for_admin_custom_field_settings_custom_fields_id_field_defaults_get(
        self, id: str, fields: str = None
    ) -> Awaitable[m.CustomFieldDefaults]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.CustomFieldDefaults,
            method="GET",
            url="/admin/customFieldSettings/customFields/{id}/fieldDefaults",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_custom_fields_id_field_defaults_post(
        self, id: str, fields: str = None, custom_field_defaults: m.CustomFieldDefaults = None
    ) -> Awaitable[m.CustomFieldDefaults]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(custom_field_defaults)

        return self.api_client.request(
            type_=m.CustomFieldDefaults,
            method="POST",
            url="/admin/customFieldSettings/customFields/{id}/fieldDefaults",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_custom_fields_id_get(
        self, id: str, fields: str = None
    ) -> Awaitable[m.CustomField]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.CustomField,
            method="GET",
            url="/admin/customFieldSettings/customFields/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_custom_fields_id_instances_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.ProjectCustomField]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.ProjectCustomField],
            method="GET",
            url="/admin/customFieldSettings/customFields/{id}/instances",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_custom_field_settings_custom_fields_id_post(
        self, id: str, fields: str = None, custom_field: m.CustomField = None
    ) -> Awaitable[m.CustomField]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(custom_field)

        return self.api_client.request(
            type_=m.CustomField,
            method="POST",
            url="/admin/customFieldSettings/customFields/{id}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_custom_fields_post(
        self, fields: str = None, custom_field: m.CustomField = None
    ) -> Awaitable[m.CustomField]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(custom_field)

        return self.api_client.request(
            type_=m.CustomField,
            method="POST",
            url="/admin/customFieldSettings/customFields",
            params=query_params,
            json=body,
        )

    def _build_for_admin_custom_field_settings_types_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.FieldType]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.FieldType],
            method="GET",
            url="/admin/customFieldSettings/types",
            params=query_params,
        )

    def _build_for_admin_database_backup_backups_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.BackupFile]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.BackupFile],
            method="GET",
            url="/admin/databaseBackup/backups",
            params=query_params,
        )

    def _build_for_admin_database_backup_backups_id_get(self, id: str, fields: str = None) -> Awaitable[m.BackupFile]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.BackupFile,
            method="GET",
            url="/admin/databaseBackup/backups/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_database_backup_settings_backup_status_get(
        self, fields: str = None
    ) -> Awaitable[m.BackupStatus]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.BackupStatus,
            method="GET",
            url="/admin/databaseBackup/settings/backupStatus",
            params=query_params,
        )

    def _build_for_admin_database_backup_settings_get(self, fields: str = None) -> Awaitable[m.DatabaseBackupSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.DatabaseBackupSettings,
            method="GET",
            url="/admin/databaseBackup/settings",
            params=query_params,
        )

    def _build_for_admin_database_backup_settings_post(
        self, fields: str = None, database_backup_settings: m.DatabaseBackupSettings = None
    ) -> Awaitable[m.DatabaseBackupSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(database_backup_settings)

        return self.api_client.request(
            type_=m.DatabaseBackupSettings,
            method="POST",
            url="/admin/databaseBackup/settings",
            params=query_params,
            json=body,
        )

    def _build_for_admin_global_settings_appearance_settings_get(
        self, fields: str = None
    ) -> Awaitable[m.AppearanceSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.AppearanceSettings,
            method="GET",
            url="/admin/globalSettings/appearanceSettings",
            params=query_params,
        )

    def _build_for_admin_global_settings_appearance_settings_post(
        self, fields: str = None, appearance_settings: m.AppearanceSettings = None
    ) -> Awaitable[m.AppearanceSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(appearance_settings)

        return self.api_client.request(
            type_=m.AppearanceSettings,
            method="POST",
            url="/admin/globalSettings/appearanceSettings",
            params=query_params,
            json=body,
        )

    def _build_for_admin_global_settings_get(self, fields: str = None) -> Awaitable[m.GlobalSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.GlobalSettings,
            method="GET",
            url="/admin/globalSettings",
            params=query_params,
        )

    def _build_for_admin_global_settings_license_get(self, fields: str = None) -> Awaitable[m.License]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.License,
            method="GET",
            url="/admin/globalSettings/license",
            params=query_params,
        )

    def _build_for_admin_global_settings_license_post(
        self, fields: str = None, license: m.License = None
    ) -> Awaitable[m.License]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(license)

        return self.api_client.request(
            type_=m.License, method="POST", url="/admin/globalSettings/license", params=query_params, json=body
        )

    def _build_for_admin_global_settings_locale_settings_get(self, fields: str = None) -> Awaitable[m.LocaleSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.LocaleSettings,
            method="GET",
            url="/admin/globalSettings/localeSettings",
            params=query_params,
        )

    def _build_for_admin_global_settings_locale_settings_post(
        self, fields: str = None, locale_settings: m.LocaleSettings = None
    ) -> Awaitable[m.LocaleSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(locale_settings)

        return self.api_client.request(
            type_=m.LocaleSettings,
            method="POST",
            url="/admin/globalSettings/localeSettings",
            params=query_params,
            json=body,
        )

    def _build_for_admin_global_settings_notification_settings_get(
        self, fields: str = None
    ) -> Awaitable[m.NotificationSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.NotificationSettings,
            method="GET",
            url="/admin/globalSettings/notificationSettings",
            params=query_params,
        )

    def _build_for_admin_global_settings_notification_settings_post(
        self, fields: str = None, notification_settings: m.NotificationSettings = None
    ) -> Awaitable[m.NotificationSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(notification_settings)

        return self.api_client.request(
            type_=m.NotificationSettings,
            method="POST",
            url="/admin/globalSettings/notificationSettings",
            params=query_params,
            json=body,
        )

    def _build_for_admin_global_settings_post(
        self, fields: str = None, global_settings: m.GlobalSettings = None
    ) -> Awaitable[m.GlobalSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(global_settings)

        return self.api_client.request(
            type_=m.GlobalSettings, method="POST", url="/admin/globalSettings", params=query_params, json=body
        )

    def _build_for_admin_global_settings_rest_settings_get(self, fields: str = None) -> Awaitable[m.RestCorsSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.RestCorsSettings,
            method="GET",
            url="/admin/globalSettings/restSettings",
            params=query_params,
        )

    def _build_for_admin_global_settings_rest_settings_post(
        self, fields: str = None, rest_cors_settings: m.RestCorsSettings = None
    ) -> Awaitable[m.RestCorsSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(rest_cors_settings)

        return self.api_client.request(
            type_=m.RestCorsSettings,
            method="POST",
            url="/admin/globalSettings/restSettings",
            params=query_params,
            json=body,
        )

    def _build_for_admin_global_settings_system_settings_get(self, fields: str = None) -> Awaitable[m.SystemSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.SystemSettings,
            method="GET",
            url="/admin/globalSettings/systemSettings",
            params=query_params,
        )

    def _build_for_admin_global_settings_system_settings_post(
        self, fields: str = None, system_settings: m.SystemSettings = None
    ) -> Awaitable[m.SystemSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(system_settings)

        return self.api_client.request(
            type_=m.SystemSettings,
            method="POST",
            url="/admin/globalSettings/systemSettings",
            params=query_params,
            json=body,
        )

    def _build_for_admin_projects_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.Project]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.Project],
            method="GET",
            url="/admin/projects",
            params=query_params,
        )

    def _build_for_admin_projects_id_custom_fields_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.ProjectCustomField]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.ProjectCustomField],
            method="GET",
            url="/admin/projects/{id}/customFields",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_projects_id_custom_fields_post(
        self, id: str, fields: str = None, project_custom_field: m.ProjectCustomField = None
    ) -> Awaitable[m.ProjectCustomField]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(project_custom_field)

        return self.api_client.request(
            type_=m.ProjectCustomField,
            method="POST",
            url="/admin/projects/{id}/customFields",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_projects_id_custom_fields_project_custom_field_id_delete(
        self, id: str, project_custom_field_id: str
    ) -> Awaitable[None]:
        path_params = {"id": str(id), "projectCustomFieldId": str(project_custom_field_id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/projects/{id}/customFields/{projectCustomFieldId}",
            path_params=path_params,
        )

    def _build_for_admin_projects_id_custom_fields_project_custom_field_id_get(
        self, id: str, project_custom_field_id: str, fields: str = None
    ) -> Awaitable[m.ProjectCustomField]:
        path_params = {"id": str(id), "projectCustomFieldId": str(project_custom_field_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.ProjectCustomField,
            method="GET",
            url="/admin/projects/{id}/customFields/{projectCustomFieldId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_projects_id_custom_fields_project_custom_field_id_post(
        self,
        id: str,
        project_custom_field_id: str,
        fields: str = None,
        project_custom_field: m.ProjectCustomField = None,
    ) -> Awaitable[m.ProjectCustomField]:
        path_params = {"id": str(id), "projectCustomFieldId": str(project_custom_field_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(project_custom_field)

        return self.api_client.request(
            type_=m.ProjectCustomField,
            method="POST",
            url="/admin/projects/{id}/customFields/{projectCustomFieldId}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_projects_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/projects/{id}",
            path_params=path_params,
        )

    def _build_for_admin_projects_id_get(self, id: str, fields: str = None) -> Awaitable[m.Project]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.Project,
            method="GET",
            url="/admin/projects/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_projects_id_issues_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.Issue]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.Issue],
            method="GET",
            url="/admin/projects/{id}/issues",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_projects_id_issues_issue_id_delete(self, id: str, issue_id: str) -> Awaitable[None]:
        path_params = {"id": str(id), "issueId": str(issue_id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/projects/{id}/issues/{issueId}",
            path_params=path_params,
        )

    def _build_for_admin_projects_id_issues_issue_id_get(
        self, id: str, issue_id: str, fields: str = None
    ) -> Awaitable[m.Issue]:
        path_params = {"id": str(id), "issueId": str(issue_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.Issue,
            method="GET",
            url="/admin/projects/{id}/issues/{issueId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_projects_id_issues_issue_id_post(
        self, id: str, issue_id: str, fields: str = None, issue: m.Issue = None
    ) -> Awaitable[m.Issue]:
        path_params = {"id": str(id), "issueId": str(issue_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue)

        return self.api_client.request(
            type_=m.Issue,
            method="POST",
            url="/admin/projects/{id}/issues/{issueId}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_projects_id_issues_post(
        self, id: str, fields: str = None, issue: m.Issue = None
    ) -> Awaitable[m.Issue]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue)

        return self.api_client.request(
            type_=m.Issue,
            method="POST",
            url="/admin/projects/{id}/issues",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_projects_id_post(
        self, id: str, fields: str = None, project: m.Project = None
    ) -> Awaitable[m.Project]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(project)

        return self.api_client.request(
            type_=m.Project,
            method="POST",
            url="/admin/projects/{id}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_projects_id_time_tracking_settings_get(
        self, id: str, fields: str = None
    ) -> Awaitable[m.ProjectTimeTrackingSettings]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.ProjectTimeTrackingSettings,
            method="GET",
            url="/admin/projects/{id}/timeTrackingSettings",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_projects_id_time_tracking_settings_post(
        self, id: str, fields: str = None, project_time_tracking_settings: m.ProjectTimeTrackingSettings = None
    ) -> Awaitable[m.ProjectTimeTrackingSettings]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(project_time_tracking_settings)

        return self.api_client.request(
            type_=m.ProjectTimeTrackingSettings,
            method="POST",
            url="/admin/projects/{id}/timeTrackingSettings",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_projects_id_time_tracking_settings_work_item_types_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.WorkItemType]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.WorkItemType],
            method="GET",
            url="/admin/projects/{id}/timeTrackingSettings/workItemTypes",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_projects_id_time_tracking_settings_work_item_types_post(
        self, id: str, fields: str = None, work_item_type: m.WorkItemType = None
    ) -> Awaitable[m.WorkItemType]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(work_item_type)

        return self.api_client.request(
            type_=m.WorkItemType,
            method="POST",
            url="/admin/projects/{id}/timeTrackingSettings/workItemTypes",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_delete(
        self, id: str, work_item_type_id: str
    ) -> Awaitable[None]:
        path_params = {"id": str(id), "workItemTypeId": str(work_item_type_id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/projects/{id}/timeTrackingSettings/workItemTypes/{workItemTypeId}",
            path_params=path_params,
        )

    def _build_for_admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_get(
        self, id: str, work_item_type_id: str, fields: str = None
    ) -> Awaitable[m.WorkItemType]:
        path_params = {"id": str(id), "workItemTypeId": str(work_item_type_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.WorkItemType,
            method="GET",
            url="/admin/projects/{id}/timeTrackingSettings/workItemTypes/{workItemTypeId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_projects_post(
        self, template: str = None, fields: str = None, project: m.Project = None
    ) -> Awaitable[m.Project]:
        query_params = {}
        if template is not None:
            query_params["template"] = str(template)
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(project)

        return self.api_client.request(
            type_=m.Project, method="POST", url="/admin/projects", params=query_params, json=body
        )

    def _build_for_admin_telemetry_get(self, fields: str = None) -> Awaitable[m.Telemetry]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.Telemetry,
            method="GET",
            url="/admin/telemetry",
            params=query_params,
        )

    def _build_for_admin_time_tracking_settings_get(
        self, fields: str = None
    ) -> Awaitable[m.GlobalTimeTrackingSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.GlobalTimeTrackingSettings,
            method="GET",
            url="/admin/timeTrackingSettings",
            params=query_params,
        )

    def _build_for_admin_time_tracking_settings_work_item_types_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.WorkItemType]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.WorkItemType],
            method="GET",
            url="/admin/timeTrackingSettings/workItemTypes",
            params=query_params,
        )

    def _build_for_admin_time_tracking_settings_work_item_types_post(
        self, fields: str = None, work_item_type: m.WorkItemType = None
    ) -> Awaitable[m.WorkItemType]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(work_item_type)

        return self.api_client.request(
            type_=m.WorkItemType,
            method="POST",
            url="/admin/timeTrackingSettings/workItemTypes",
            params=query_params,
            json=body,
        )

    def _build_for_admin_time_tracking_settings_work_item_types_work_item_type_id_delete(
        self, work_item_type_id: str
    ) -> Awaitable[None]:
        path_params = {"workItemTypeId": str(work_item_type_id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/admin/timeTrackingSettings/workItemTypes/{workItemTypeId}",
            path_params=path_params,
        )

    def _build_for_admin_time_tracking_settings_work_item_types_work_item_type_id_get(
        self, work_item_type_id: str, fields: str = None
    ) -> Awaitable[m.WorkItemType]:
        path_params = {"workItemTypeId": str(work_item_type_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.WorkItemType,
            method="GET",
            url="/admin/timeTrackingSettings/workItemTypes/{workItemTypeId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_admin_time_tracking_settings_work_item_types_work_item_type_id_post(
        self, work_item_type_id: str, fields: str = None, work_item_type: m.WorkItemType = None
    ) -> Awaitable[m.WorkItemType]:
        path_params = {"workItemTypeId": str(work_item_type_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(work_item_type)

        return self.api_client.request(
            type_=m.WorkItemType,
            method="POST",
            url="/admin/timeTrackingSettings/workItemTypes/{workItemTypeId}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_admin_time_tracking_settings_work_time_settings_get(
        self, fields: str = None
    ) -> Awaitable[m.WorkTimeSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.WorkTimeSettings,
            method="GET",
            url="/admin/timeTrackingSettings/workTimeSettings",
            params=query_params,
        )

    def _build_for_admin_time_tracking_settings_work_time_settings_post(
        self, fields: str = None, work_time_settings: m.WorkTimeSettings = None
    ) -> Awaitable[m.WorkTimeSettings]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(work_time_settings)

        return self.api_client.request(
            type_=m.WorkTimeSettings,
            method="POST",
            url="/admin/timeTrackingSettings/workTimeSettings",
            params=query_params,
            json=body,
        )

    def _build_for_agiles_get(self, fields: str = None, skip: int = None, top: int = None) -> Awaitable[List[m.Agile]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.Agile],
            method="GET",
            url="/agiles",
            params=query_params,
        )

    def _build_for_agiles_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/agiles/{id}",
            path_params=path_params,
        )

    def _build_for_agiles_id_get(self, id: str, fields: str = None) -> Awaitable[m.Agile]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.Agile,
            method="GET",
            url="/agiles/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_agiles_id_post(self, id: str, fields: str = None, agile: m.Agile = None) -> Awaitable[m.Agile]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(agile)

        return self.api_client.request(
            type_=m.Agile, method="POST", url="/agiles/{id}", path_params=path_params, params=query_params, json=body
        )

    def _build_for_agiles_id_sprints_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.Sprint]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.Sprint],
            method="GET",
            url="/agiles/{id}/sprints",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_agiles_id_sprints_post(
        self, id: str, fields: str = None, sprint: m.Sprint = None
    ) -> Awaitable[m.Sprint]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(sprint)

        return self.api_client.request(
            type_=m.Sprint,
            method="POST",
            url="/agiles/{id}/sprints",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_agiles_id_sprints_sprint_id_delete(self, id: str, sprint_id: str) -> Awaitable[None]:
        path_params = {"id": str(id), "sprintId": str(sprint_id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/agiles/{id}/sprints/{sprintId}",
            path_params=path_params,
        )

    def _build_for_agiles_id_sprints_sprint_id_get(
        self, id: str, sprint_id: str, fields: str = None
    ) -> Awaitable[m.Sprint]:
        path_params = {"id": str(id), "sprintId": str(sprint_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.Sprint,
            method="GET",
            url="/agiles/{id}/sprints/{sprintId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_agiles_id_sprints_sprint_id_post(
        self, id: str, sprint_id: str, fields: str = None, sprint: m.Sprint = None
    ) -> Awaitable[m.Sprint]:
        path_params = {"id": str(id), "sprintId": str(sprint_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(sprint)

        return self.api_client.request(
            type_=m.Sprint,
            method="POST",
            url="/agiles/{id}/sprints/{sprintId}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_agiles_post(
        self, template: str = None, fields: str = None, agile: m.Agile = None
    ) -> Awaitable[m.Agile]:
        query_params = {}
        if template is not None:
            query_params["template"] = str(template)
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(agile)

        return self.api_client.request(type_=m.Agile, method="POST", url="/agiles", params=query_params, json=body)

    def _build_for_groups_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.UserGroup]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.UserGroup],
            method="GET",
            url="/groups",
            params=query_params,
        )

    def _build_for_groups_id_get(self, id: str, fields: str = None) -> Awaitable[m.UserGroup]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.UserGroup,
            method="GET",
            url="/groups/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issue_link_types_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.IssueLinkType]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.IssueLinkType],
            method="GET",
            url="/issueLinkTypes",
            params=query_params,
        )

    def _build_for_issue_link_types_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/issueLinkTypes/{id}",
            path_params=path_params,
        )

    def _build_for_issue_link_types_id_get(self, id: str, fields: str = None) -> Awaitable[m.IssueLinkType]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.IssueLinkType,
            method="GET",
            url="/issueLinkTypes/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issue_link_types_id_post(
        self, id: str, fields: str = None, issue_link_type: m.IssueLinkType = None
    ) -> Awaitable[m.IssueLinkType]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue_link_type)

        return self.api_client.request(
            type_=m.IssueLinkType,
            method="POST",
            url="/issueLinkTypes/{id}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_issue_link_types_post(
        self, fields: str = None, issue_link_type: m.IssueLinkType = None
    ) -> Awaitable[m.IssueLinkType]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue_link_type)

        return self.api_client.request(
            type_=m.IssueLinkType, method="POST", url="/issueLinkTypes", params=query_params, json=body
        )

    def _build_for_issue_tags_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.IssueTag]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.IssueTag],
            method="GET",
            url="/issueTags",
            params=query_params,
        )

    def _build_for_issue_tags_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/issueTags/{id}",
            path_params=path_params,
        )

    def _build_for_issue_tags_id_get(self, id: str, fields: str = None) -> Awaitable[m.IssueTag]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.IssueTag,
            method="GET",
            url="/issueTags/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issue_tags_id_issues_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.Issue]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.Issue],
            method="GET",
            url="/issueTags/{id}/issues",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issue_tags_id_post(
        self, id: str, fields: str = None, issue_tag: m.IssueTag = None
    ) -> Awaitable[m.IssueTag]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue_tag)

        return self.api_client.request(
            type_=m.IssueTag,
            method="POST",
            url="/issueTags/{id}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_issue_tags_post(self, fields: str = None, issue_tag: m.IssueTag = None) -> Awaitable[m.IssueTag]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue_tag)

        return self.api_client.request(
            type_=m.IssueTag, method="POST", url="/issueTags", params=query_params, json=body
        )

    def _build_for_issues_get(
        self, query: str = None, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.Issue]]:
        query_params = {}
        if query is not None:
            query_params["query"] = str(query)
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.Issue],
            method="GET",
            url="/issues",
            params=query_params,
        )

    def _build_for_issues_id_activities_activity_item_id_get(
        self, id: str, activity_item_id: str, fields: str = None
    ) -> Awaitable[m.ActivityItem]:
        path_params = {"id": str(id), "activityItemId": str(activity_item_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.ActivityItem,
            method="GET",
            url="/issues/{id}/activities/{activityItemId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_activities_get(
        self,
        id: str,
        categories: str = None,
        reverse: bool = None,
        start: str = None,
        end: str = None,
        author: str = None,
        fields: str = None,
        skip: int = None,
        top: int = None,
    ) -> Awaitable[List[m.ActivityItem]]:
        path_params = {"id": str(id)}

        query_params = {}
        if categories is not None:
            query_params["categories"] = str(categories)
        if reverse is not None:
            query_params["reverse"] = str(reverse)
        if start is not None:
            query_params["start"] = str(start)
        if end is not None:
            query_params["end"] = str(end)
        if author is not None:
            query_params["author"] = str(author)
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.ActivityItem],
            method="GET",
            url="/issues/{id}/activities",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_activities_page_get(
        self,
        id: str,
        categories: str = None,
        reverse: bool = None,
        start: str = None,
        end: str = None,
        author: str = None,
        cursor: str = None,
        activity_id: str = None,
        fields: str = None,
    ) -> Awaitable[m.ActivityCursorPage]:
        path_params = {"id": str(id)}

        query_params = {}
        if categories is not None:
            query_params["categories"] = str(categories)
        if reverse is not None:
            query_params["reverse"] = str(reverse)
        if start is not None:
            query_params["start"] = str(start)
        if end is not None:
            query_params["end"] = str(end)
        if author is not None:
            query_params["author"] = str(author)
        if cursor is not None:
            query_params["cursor"] = str(cursor)
        if activity_id is not None:
            query_params["activityId"] = str(activity_id)
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.ActivityCursorPage,
            method="GET",
            url="/issues/{id}/activitiesPage",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_attachments_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.IssueAttachment]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.IssueAttachment],
            method="GET",
            url="/issues/{id}/attachments",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_attachments_issue_attachment_id_delete(
        self, id: str, issue_attachment_id: str
    ) -> Awaitable[None]:
        path_params = {"id": str(id), "issueAttachmentId": str(issue_attachment_id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/issues/{id}/attachments/{issueAttachmentId}",
            path_params=path_params,
        )

    def _build_for_issues_id_attachments_issue_attachment_id_get(
        self, id: str, issue_attachment_id: str, fields: str = None
    ) -> Awaitable[m.IssueAttachment]:
        path_params = {"id": str(id), "issueAttachmentId": str(issue_attachment_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.IssueAttachment,
            method="GET",
            url="/issues/{id}/attachments/{issueAttachmentId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_attachments_issue_attachment_id_post(
        self, id: str, issue_attachment_id: str, fields: str = None, issue_attachment: m.IssueAttachment = None
    ) -> Awaitable[m.IssueAttachment]:
        path_params = {"id": str(id), "issueAttachmentId": str(issue_attachment_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue_attachment)

        return self.api_client.request(
            type_=m.IssueAttachment,
            method="POST",
            url="/issues/{id}/attachments/{issueAttachmentId}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_issues_id_attachments_post(
        self, id: str, fields: str = None, issue_attachment: m.IssueAttachment = None
    ) -> Awaitable[m.IssueAttachment]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue_attachment)

        return self.api_client.request(
            type_=m.IssueAttachment,
            method="POST",
            url="/issues/{id}/attachments",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_issues_id_comments_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.IssueComment]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.IssueComment],
            method="GET",
            url="/issues/{id}/comments",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_comments_issue_comment_id_delete(self, id: str, issue_comment_id: str) -> Awaitable[None]:
        path_params = {"id": str(id), "issueCommentId": str(issue_comment_id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/issues/{id}/comments/{issueCommentId}",
            path_params=path_params,
        )

    def _build_for_issues_id_comments_issue_comment_id_get(
        self, id: str, issue_comment_id: str, fields: str = None
    ) -> Awaitable[m.IssueComment]:
        path_params = {"id": str(id), "issueCommentId": str(issue_comment_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.IssueComment,
            method="GET",
            url="/issues/{id}/comments/{issueCommentId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_comments_issue_comment_id_post(
        self, id: str, issue_comment_id: str, fields: str = None, issue_comment: m.IssueComment = None
    ) -> Awaitable[m.IssueComment]:
        path_params = {"id": str(id), "issueCommentId": str(issue_comment_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue_comment)

        return self.api_client.request(
            type_=m.IssueComment,
            method="POST",
            url="/issues/{id}/comments/{issueCommentId}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_issues_id_comments_post(
        self, id: str, draft_id: str = None, fields: str = None, issue_comment: m.IssueComment = None
    ) -> Awaitable[m.IssueComment]:
        path_params = {"id": str(id)}

        query_params = {}
        if draft_id is not None:
            query_params["draftId"] = str(draft_id)
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue_comment)

        return self.api_client.request(
            type_=m.IssueComment,
            method="POST",
            url="/issues/{id}/comments",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_issues_id_custom_fields_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.IssueCustomField]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.IssueCustomField],
            method="GET",
            url="/issues/{id}/customFields",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_custom_fields_issue_custom_field_id_get(
        self, id: str, issue_custom_field_id: str, fields: str = None
    ) -> Awaitable[m.IssueCustomField]:
        path_params = {"id": str(id), "issueCustomFieldId": str(issue_custom_field_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.IssueCustomField,
            method="GET",
            url="/issues/{id}/customFields/{issueCustomFieldId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_custom_fields_issue_custom_field_id_post(
        self, id: str, issue_custom_field_id: str, fields: str = None, issue_custom_field: m.IssueCustomField = None
    ) -> Awaitable[m.IssueCustomField]:
        path_params = {"id": str(id), "issueCustomFieldId": str(issue_custom_field_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue_custom_field)

        return self.api_client.request(
            type_=m.IssueCustomField,
            method="POST",
            url="/issues/{id}/customFields/{issueCustomFieldId}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_issues_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/issues/{id}",
            path_params=path_params,
        )

    def _build_for_issues_id_get(self, id: str, fields: str = None) -> Awaitable[m.Issue]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.Issue,
            method="GET",
            url="/issues/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_links_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.IssueLink]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.IssueLink],
            method="GET",
            url="/issues/{id}/links",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_links_issue_link_id_get(
        self, id: str, issue_link_id: str, fields: str = None
    ) -> Awaitable[m.IssueLink]:
        path_params = {"id": str(id), "issueLinkId": str(issue_link_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.IssueLink,
            method="GET",
            url="/issues/{id}/links/{issueLinkId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_links_issue_link_id_issues_get(
        self, id: str, issue_link_id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.Issue]]:
        path_params = {"id": str(id), "issueLinkId": str(issue_link_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.Issue],
            method="GET",
            url="/issues/{id}/links/{issueLinkId}/issues",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_links_issue_link_id_issues_issue_id_delete(
        self, id: str, issue_link_id: str, issue_id: str
    ) -> Awaitable[None]:
        path_params = {"id": str(id), "issueLinkId": str(issue_link_id), "issueId": str(issue_id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/issues/{id}/links/{issueLinkId}/issues/{issueId}",
            path_params=path_params,
        )

    def _build_for_issues_id_links_issue_link_id_issues_post(
        self, id: str, issue_link_id: str, fields: str = None, issue: m.Issue = None
    ) -> Awaitable[m.Issue]:
        path_params = {"id": str(id), "issueLinkId": str(issue_link_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue)

        return self.api_client.request(
            type_=m.Issue,
            method="POST",
            url="/issues/{id}/links/{issueLinkId}/issues",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_issues_id_post(self, id: str, fields: str = None, issue: m.Issue = None) -> Awaitable[m.Issue]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue)

        return self.api_client.request(
            type_=m.Issue, method="POST", url="/issues/{id}", path_params=path_params, params=query_params, json=body
        )

    def _build_for_issues_id_project_get(self, id: str, fields: str = None) -> Awaitable[m.Project]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.Project,
            method="GET",
            url="/issues/{id}/project",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_project_post(
        self, id: str, fields: str = None, project: m.Project = None
    ) -> Awaitable[m.Project]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(project)

        return self.api_client.request(
            type_=m.Project,
            method="POST",
            url="/issues/{id}/project",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_issues_id_time_tracking_get(self, id: str, fields: str = None) -> Awaitable[m.IssueTimeTracker]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.IssueTimeTracker,
            method="GET",
            url="/issues/{id}/timeTracking",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_time_tracking_work_items_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.IssueWorkItem]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.IssueWorkItem],
            method="GET",
            url="/issues/{id}/timeTracking/workItems",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_time_tracking_work_items_issue_work_item_id_delete(
        self, id: str, issue_work_item_id: str
    ) -> Awaitable[None]:
        path_params = {"id": str(id), "issueWorkItemId": str(issue_work_item_id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/issues/{id}/timeTracking/workItems/{issueWorkItemId}",
            path_params=path_params,
        )

    def _build_for_issues_id_time_tracking_work_items_issue_work_item_id_get(
        self, id: str, issue_work_item_id: str, fields: str = None
    ) -> Awaitable[m.IssueWorkItem]:
        path_params = {"id": str(id), "issueWorkItemId": str(issue_work_item_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.IssueWorkItem,
            method="GET",
            url="/issues/{id}/timeTracking/workItems/{issueWorkItemId}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_issues_id_time_tracking_work_items_issue_work_item_id_post(
        self, id: str, issue_work_item_id: str, fields: str = None, issue_work_item: m.IssueWorkItem = None
    ) -> Awaitable[m.IssueWorkItem]:
        path_params = {"id": str(id), "issueWorkItemId": str(issue_work_item_id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue_work_item)

        return self.api_client.request(
            type_=m.IssueWorkItem,
            method="POST",
            url="/issues/{id}/timeTracking/workItems/{issueWorkItemId}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_issues_id_time_tracking_work_items_post(
        self, id: str, fields: str = None, issue_work_item: m.IssueWorkItem = None
    ) -> Awaitable[m.IssueWorkItem]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue_work_item)

        return self.api_client.request(
            type_=m.IssueWorkItem,
            method="POST",
            url="/issues/{id}/timeTracking/workItems",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_issues_post(
        self, draft_id: str = None, fields: str = None, issue: m.Issue = None
    ) -> Awaitable[m.Issue]:
        query_params = {}
        if draft_id is not None:
            query_params["draftId"] = str(draft_id)
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(issue)

        return self.api_client.request(type_=m.Issue, method="POST", url="/issues", params=query_params, json=body)

    def _build_for_saved_queries_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.SavedQuery]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.SavedQuery],
            method="GET",
            url="/savedQueries",
            params=query_params,
        )

    def _build_for_saved_queries_id_delete(self, id: str) -> Awaitable[None]:
        path_params = {"id": str(id)}

        return self.api_client.request(
            type_=None,
            method="DELETE",
            url="/savedQueries/{id}",
            path_params=path_params,
        )

    def _build_for_saved_queries_id_get(self, id: str, fields: str = None) -> Awaitable[m.SavedQuery]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.SavedQuery,
            method="GET",
            url="/savedQueries/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_saved_queries_id_post(
        self, id: str, fields: str = None, saved_query: m.SavedQuery = None
    ) -> Awaitable[m.SavedQuery]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(saved_query)

        return self.api_client.request(
            type_=m.SavedQuery,
            method="POST",
            url="/savedQueries/{id}",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_saved_queries_post(
        self, fields: str = None, saved_query: m.SavedQuery = None
    ) -> Awaitable[m.SavedQuery]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(saved_query)

        return self.api_client.request(
            type_=m.SavedQuery, method="POST", url="/savedQueries", params=query_params, json=body
        )

    def _build_for_users_get(self, fields: str = None, skip: int = None, top: int = None) -> Awaitable[List[m.User]]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.User],
            method="GET",
            url="/users",
            params=query_params,
        )

    def _build_for_users_id_get(self, id: str, fields: str = None) -> Awaitable[m.User]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.User,
            method="GET",
            url="/users/{id}",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_users_id_profiles_general_get(self, id: str, fields: str = None) -> Awaitable[m.GeneralUserProfile]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.GeneralUserProfile,
            method="GET",
            url="/users/{id}/profiles/general",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_users_id_profiles_general_post(
        self, id: str, fields: str = None, general_user_profile: m.GeneralUserProfile = None
    ) -> Awaitable[m.GeneralUserProfile]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(general_user_profile)

        return self.api_client.request(
            type_=m.GeneralUserProfile,
            method="POST",
            url="/users/{id}/profiles/general",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_users_id_profiles_notifications_get(
        self, id: str, fields: str = None
    ) -> Awaitable[m.NotificationsUserProfile]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.NotificationsUserProfile,
            method="GET",
            url="/users/{id}/profiles/notifications",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_users_id_profiles_notifications_post(
        self, id: str, fields: str = None, notifications_user_profile: m.NotificationsUserProfile = None
    ) -> Awaitable[m.NotificationsUserProfile]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(notifications_user_profile)

        return self.api_client.request(
            type_=m.NotificationsUserProfile,
            method="POST",
            url="/users/{id}/profiles/notifications",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_users_id_profiles_timetracking_get(
        self, id: str, fields: str = None
    ) -> Awaitable[m.TimeTrackingUserProfile]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.TimeTrackingUserProfile,
            method="GET",
            url="/users/{id}/profiles/timetracking",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_users_id_profiles_timetracking_post(
        self, id: str, fields: str = None, time_tracking_user_profile: m.TimeTrackingUserProfile = None
    ) -> Awaitable[m.TimeTrackingUserProfile]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        body = jsonable_encoder(time_tracking_user_profile)

        return self.api_client.request(
            type_=m.TimeTrackingUserProfile,
            method="POST",
            url="/users/{id}/profiles/timetracking",
            path_params=path_params,
            params=query_params,
            json=body,
        )

    def _build_for_users_id_saved_queries_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.SavedQuery]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.SavedQuery],
            method="GET",
            url="/users/{id}/savedQueries",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_users_id_tags_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> Awaitable[List[m.IssueTag]]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.IssueTag],
            method="GET",
            url="/users/{id}/tags",
            path_params=path_params,
            params=query_params,
        )

    def _build_for_users_me_get(self, fields: str = None) -> Awaitable[m.Me]:
        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.Me,
            method="GET",
            url="/users/me",
            params=query_params,
        )

    def _build_for_work_items_get(
        self,
        query: str = None,
        start_date: date = None,
        end_date: date = None,
        start: int = None,
        end: int = None,
        created_start: int = None,
        created_end: int = None,
        updated_start: int = None,
        updated_end: int = None,
        author: str = None,
        creator: str = None,
        fields: str = None,
        skip: int = None,
        top: int = None,
    ) -> Awaitable[List[m.IssueWorkItem]]:
        query_params = {}
        if query is not None:
            query_params["query"] = str(query)
        if start_date is not None:
            query_params["startDate"] = str(start_date)
        if end_date is not None:
            query_params["endDate"] = str(end_date)
        if start is not None:
            query_params["start"] = str(start)
        if end is not None:
            query_params["end"] = str(end)
        if created_start is not None:
            query_params["createdStart"] = str(created_start)
        if created_end is not None:
            query_params["createdEnd"] = str(created_end)
        if updated_start is not None:
            query_params["updatedStart"] = str(updated_start)
        if updated_end is not None:
            query_params["updatedEnd"] = str(updated_end)
        if author is not None:
            query_params["author"] = str(author)
        if creator is not None:
            query_params["creator"] = str(creator)
        if fields is not None:
            query_params["fields"] = str(fields)
        if skip is not None:
            query_params["$skip"] = str(skip)
        if top is not None:
            query_params["$top"] = str(top)

        return self.api_client.request(
            type_=List[m.IssueWorkItem],
            method="GET",
            url="/workItems",
            params=query_params,
        )

    def _build_for_work_items_id_get(self, id: str, fields: str = None) -> Awaitable[m.IssueWorkItem]:
        path_params = {"id": str(id)}

        query_params = {}
        if fields is not None:
            query_params["fields"] = str(fields)

        return self.api_client.request(
            type_=m.IssueWorkItem,
            method="GET",
            url="/workItems/{id}",
            path_params=path_params,
            params=query_params,
        )


class AsyncDefaultApi(_DefaultApi):
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.api_client.close()

    async def activities_get(
        self,
        categories: str = None,
        reverse: bool = None,
        start: str = None,
        end: str = None,
        author: str = None,
        issue_query: str = None,
        fields: str = None,
        skip: int = None,
        top: int = None,
    ) -> List[m.ActivityItem]:
        return await self._build_for_activities_get(
            categories=categories,
            reverse=reverse,
            start=start,
            end=end,
            author=author,
            issue_query=issue_query,
            fields=fields,
            skip=skip,
            top=top,
        )

    async def activities_id_get(self, id: str, fields: str = None) -> m.ActivityItem:
        return await self._build_for_activities_id_get(id=id, fields=fields)

    async def activities_page_get(
        self,
        categories: str = None,
        reverse: bool = None,
        start: str = None,
        end: str = None,
        author: str = None,
        issue_query: str = None,
        cursor: str = None,
        activity_id: str = None,
        fields: str = None,
    ) -> m.ActivityCursorPage:
        return await self._build_for_activities_page_get(
            categories=categories,
            reverse=reverse,
            start=start,
            end=end,
            author=author,
            issue_query=issue_query,
            cursor=cursor,
            activity_id=activity_id,
            fields=fields,
        )

    async def admin_custom_field_settings_bundles_build_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.BuildBundle]:
        return await self._build_for_admin_custom_field_settings_bundles_build_get(fields=fields, skip=skip, top=top)

    async def admin_custom_field_settings_bundles_build_id_delete(self, id: str) -> None:
        return await self._build_for_admin_custom_field_settings_bundles_build_id_delete(id=id)

    async def admin_custom_field_settings_bundles_build_id_get(self, id: str, fields: str = None) -> m.BuildBundle:
        return await self._build_for_admin_custom_field_settings_bundles_build_id_get(id=id, fields=fields)

    async def admin_custom_field_settings_bundles_build_id_post(
        self, id: str, fields: str = None, build_bundle: m.BuildBundle = None
    ) -> m.BuildBundle:
        return await self._build_for_admin_custom_field_settings_bundles_build_id_post(
            id=id, fields=fields, build_bundle=build_bundle
        )

    async def admin_custom_field_settings_bundles_build_post(
        self, fields: str = None, build_bundle: m.BuildBundle = None
    ) -> m.BuildBundle:
        return await self._build_for_admin_custom_field_settings_bundles_build_post(
            fields=fields, build_bundle=build_bundle
        )

    async def admin_custom_field_settings_bundles_enum_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.EnumBundle]:
        return await self._build_for_admin_custom_field_settings_bundles_enum_get(fields=fields, skip=skip, top=top)

    async def admin_custom_field_settings_bundles_enum_id_delete(self, id: str) -> None:
        return await self._build_for_admin_custom_field_settings_bundles_enum_id_delete(id=id)

    async def admin_custom_field_settings_bundles_enum_id_get(self, id: str, fields: str = None) -> m.EnumBundle:
        return await self._build_for_admin_custom_field_settings_bundles_enum_id_get(id=id, fields=fields)

    async def admin_custom_field_settings_bundles_enum_id_post(
        self, id: str, fields: str = None, enum_bundle: m.EnumBundle = None
    ) -> m.EnumBundle:
        return await self._build_for_admin_custom_field_settings_bundles_enum_id_post(
            id=id, fields=fields, enum_bundle=enum_bundle
        )

    async def admin_custom_field_settings_bundles_enum_post(
        self, fields: str = None, enum_bundle: m.EnumBundle = None
    ) -> m.EnumBundle:
        return await self._build_for_admin_custom_field_settings_bundles_enum_post(
            fields=fields, enum_bundle=enum_bundle
        )

    async def admin_custom_field_settings_bundles_owned_field_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.OwnedBundle]:
        return await self._build_for_admin_custom_field_settings_bundles_owned_field_get(
            fields=fields, skip=skip, top=top
        )

    async def admin_custom_field_settings_bundles_owned_field_id_delete(self, id: str) -> None:
        return await self._build_for_admin_custom_field_settings_bundles_owned_field_id_delete(id=id)

    async def admin_custom_field_settings_bundles_owned_field_id_get(
        self, id: str, fields: str = None
    ) -> m.OwnedBundle:
        return await self._build_for_admin_custom_field_settings_bundles_owned_field_id_get(id=id, fields=fields)

    async def admin_custom_field_settings_bundles_owned_field_id_post(
        self, id: str, fields: str = None, owned_bundle: m.OwnedBundle = None
    ) -> m.OwnedBundle:
        return await self._build_for_admin_custom_field_settings_bundles_owned_field_id_post(
            id=id, fields=fields, owned_bundle=owned_bundle
        )

    async def admin_custom_field_settings_bundles_owned_field_post(
        self, fields: str = None, owned_bundle: m.OwnedBundle = None
    ) -> m.OwnedBundle:
        return await self._build_for_admin_custom_field_settings_bundles_owned_field_post(
            fields=fields, owned_bundle=owned_bundle
        )

    async def admin_custom_field_settings_bundles_state_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.StateBundle]:
        return await self._build_for_admin_custom_field_settings_bundles_state_get(fields=fields, skip=skip, top=top)

    async def admin_custom_field_settings_bundles_state_id_delete(self, id: str) -> None:
        return await self._build_for_admin_custom_field_settings_bundles_state_id_delete(id=id)

    async def admin_custom_field_settings_bundles_state_id_get(self, id: str, fields: str = None) -> m.StateBundle:
        return await self._build_for_admin_custom_field_settings_bundles_state_id_get(id=id, fields=fields)

    async def admin_custom_field_settings_bundles_state_id_post(
        self, id: str, fields: str = None, state_bundle: m.StateBundle = None
    ) -> m.StateBundle:
        return await self._build_for_admin_custom_field_settings_bundles_state_id_post(
            id=id, fields=fields, state_bundle=state_bundle
        )

    async def admin_custom_field_settings_bundles_state_post(
        self, fields: str = None, state_bundle: m.StateBundle = None
    ) -> m.StateBundle:
        return await self._build_for_admin_custom_field_settings_bundles_state_post(
            fields=fields, state_bundle=state_bundle
        )

    async def admin_custom_field_settings_bundles_user_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.UserBundle]:
        return await self._build_for_admin_custom_field_settings_bundles_user_get(fields=fields, skip=skip, top=top)

    async def admin_custom_field_settings_bundles_user_id_aggregated_users_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.User]:
        return await self._build_for_admin_custom_field_settings_bundles_user_id_aggregated_users_get(
            id=id, fields=fields, skip=skip, top=top
        )

    async def admin_custom_field_settings_bundles_user_id_delete(self, id: str) -> None:
        return await self._build_for_admin_custom_field_settings_bundles_user_id_delete(id=id)

    async def admin_custom_field_settings_bundles_user_id_get(self, id: str, fields: str = None) -> m.UserBundle:
        return await self._build_for_admin_custom_field_settings_bundles_user_id_get(id=id, fields=fields)

    async def admin_custom_field_settings_bundles_user_id_groups_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.UserGroup]:
        return await self._build_for_admin_custom_field_settings_bundles_user_id_groups_get(
            id=id, fields=fields, skip=skip, top=top
        )

    async def admin_custom_field_settings_bundles_user_id_groups_post(
        self, id: str, fields: str = None, user_group: m.UserGroup = None
    ) -> m.UserGroup:
        return await self._build_for_admin_custom_field_settings_bundles_user_id_groups_post(
            id=id, fields=fields, user_group=user_group
        )

    async def admin_custom_field_settings_bundles_user_id_groups_user_group_id_delete(
        self, id: str, user_group_id: str
    ) -> None:
        return await self._build_for_admin_custom_field_settings_bundles_user_id_groups_user_group_id_delete(
            id=id, user_group_id=user_group_id
        )

    async def admin_custom_field_settings_bundles_user_id_groups_user_group_id_get(
        self, id: str, user_group_id: str, fields: str = None
    ) -> m.UserGroup:
        return await self._build_for_admin_custom_field_settings_bundles_user_id_groups_user_group_id_get(
            id=id, user_group_id=user_group_id, fields=fields
        )

    async def admin_custom_field_settings_bundles_user_id_individuals_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.User]:
        return await self._build_for_admin_custom_field_settings_bundles_user_id_individuals_get(
            id=id, fields=fields, skip=skip, top=top
        )

    async def admin_custom_field_settings_bundles_user_id_individuals_post(
        self, id: str, fields: str = None, user: m.User = None
    ) -> m.User:
        return await self._build_for_admin_custom_field_settings_bundles_user_id_individuals_post(
            id=id, fields=fields, user=user
        )

    async def admin_custom_field_settings_bundles_user_id_individuals_user_id_delete(
        self, id: str, user_id: str
    ) -> None:
        return await self._build_for_admin_custom_field_settings_bundles_user_id_individuals_user_id_delete(
            id=id, user_id=user_id
        )

    async def admin_custom_field_settings_bundles_user_id_individuals_user_id_get(
        self, id: str, user_id: str, fields: str = None
    ) -> m.User:
        return await self._build_for_admin_custom_field_settings_bundles_user_id_individuals_user_id_get(
            id=id, user_id=user_id, fields=fields
        )

    async def admin_custom_field_settings_bundles_user_id_post(
        self, id: str, fields: str = None, user_bundle: m.UserBundle = None
    ) -> m.UserBundle:
        return await self._build_for_admin_custom_field_settings_bundles_user_id_post(
            id=id, fields=fields, user_bundle=user_bundle
        )

    async def admin_custom_field_settings_bundles_user_post(
        self, fields: str = None, user_bundle: m.UserBundle = None
    ) -> m.UserBundle:
        return await self._build_for_admin_custom_field_settings_bundles_user_post(
            fields=fields, user_bundle=user_bundle
        )

    async def admin_custom_field_settings_bundles_version_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.VersionBundle]:
        return await self._build_for_admin_custom_field_settings_bundles_version_get(fields=fields, skip=skip, top=top)

    async def admin_custom_field_settings_bundles_version_id_delete(self, id: str) -> None:
        return await self._build_for_admin_custom_field_settings_bundles_version_id_delete(id=id)

    async def admin_custom_field_settings_bundles_version_id_get(self, id: str, fields: str = None) -> m.VersionBundle:
        return await self._build_for_admin_custom_field_settings_bundles_version_id_get(id=id, fields=fields)

    async def admin_custom_field_settings_bundles_version_id_post(
        self, id: str, fields: str = None, version_bundle: m.VersionBundle = None
    ) -> m.VersionBundle:
        return await self._build_for_admin_custom_field_settings_bundles_version_id_post(
            id=id, fields=fields, version_bundle=version_bundle
        )

    async def admin_custom_field_settings_bundles_version_post(
        self, fields: str = None, version_bundle: m.VersionBundle = None
    ) -> m.VersionBundle:
        return await self._build_for_admin_custom_field_settings_bundles_version_post(
            fields=fields, version_bundle=version_bundle
        )

    async def admin_custom_field_settings_custom_fields_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.CustomField]:
        return await self._build_for_admin_custom_field_settings_custom_fields_get(fields=fields, skip=skip, top=top)

    async def admin_custom_field_settings_custom_fields_id_delete(self, id: str) -> None:
        return await self._build_for_admin_custom_field_settings_custom_fields_id_delete(id=id)

    async def admin_custom_field_settings_custom_fields_id_field_defaults_get(
        self, id: str, fields: str = None
    ) -> m.CustomFieldDefaults:
        return await self._build_for_admin_custom_field_settings_custom_fields_id_field_defaults_get(
            id=id, fields=fields
        )

    async def admin_custom_field_settings_custom_fields_id_field_defaults_post(
        self, id: str, fields: str = None, custom_field_defaults: m.CustomFieldDefaults = None
    ) -> m.CustomFieldDefaults:
        return await self._build_for_admin_custom_field_settings_custom_fields_id_field_defaults_post(
            id=id, fields=fields, custom_field_defaults=custom_field_defaults
        )

    async def admin_custom_field_settings_custom_fields_id_get(self, id: str, fields: str = None) -> m.CustomField:
        return await self._build_for_admin_custom_field_settings_custom_fields_id_get(id=id, fields=fields)

    async def admin_custom_field_settings_custom_fields_id_instances_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.ProjectCustomField]:
        return await self._build_for_admin_custom_field_settings_custom_fields_id_instances_get(
            id=id, fields=fields, skip=skip, top=top
        )

    async def admin_custom_field_settings_custom_fields_id_post(
        self, id: str, fields: str = None, custom_field: m.CustomField = None
    ) -> m.CustomField:
        return await self._build_for_admin_custom_field_settings_custom_fields_id_post(
            id=id, fields=fields, custom_field=custom_field
        )

    async def admin_custom_field_settings_custom_fields_post(
        self, fields: str = None, custom_field: m.CustomField = None
    ) -> m.CustomField:
        return await self._build_for_admin_custom_field_settings_custom_fields_post(
            fields=fields, custom_field=custom_field
        )

    async def admin_custom_field_settings_types_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.FieldType]:
        return await self._build_for_admin_custom_field_settings_types_get(fields=fields, skip=skip, top=top)

    async def admin_database_backup_backups_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.BackupFile]:
        return await self._build_for_admin_database_backup_backups_get(fields=fields, skip=skip, top=top)

    async def admin_database_backup_backups_id_get(self, id: str, fields: str = None) -> m.BackupFile:
        return await self._build_for_admin_database_backup_backups_id_get(id=id, fields=fields)

    async def admin_database_backup_settings_backup_status_get(self, fields: str = None) -> m.BackupStatus:
        return await self._build_for_admin_database_backup_settings_backup_status_get(fields=fields)

    async def admin_database_backup_settings_get(self, fields: str = None) -> m.DatabaseBackupSettings:
        return await self._build_for_admin_database_backup_settings_get(fields=fields)

    async def admin_database_backup_settings_post(
        self, fields: str = None, database_backup_settings: m.DatabaseBackupSettings = None
    ) -> m.DatabaseBackupSettings:
        return await self._build_for_admin_database_backup_settings_post(
            fields=fields, database_backup_settings=database_backup_settings
        )

    async def admin_global_settings_appearance_settings_get(self, fields: str = None) -> m.AppearanceSettings:
        return await self._build_for_admin_global_settings_appearance_settings_get(fields=fields)

    async def admin_global_settings_appearance_settings_post(
        self, fields: str = None, appearance_settings: m.AppearanceSettings = None
    ) -> m.AppearanceSettings:
        return await self._build_for_admin_global_settings_appearance_settings_post(
            fields=fields, appearance_settings=appearance_settings
        )

    async def admin_global_settings_get(self, fields: str = None) -> m.GlobalSettings:
        return await self._build_for_admin_global_settings_get(fields=fields)

    async def admin_global_settings_license_get(self, fields: str = None) -> m.License:
        return await self._build_for_admin_global_settings_license_get(fields=fields)

    async def admin_global_settings_license_post(self, fields: str = None, license: m.License = None) -> m.License:
        return await self._build_for_admin_global_settings_license_post(fields=fields, license=license)

    async def admin_global_settings_locale_settings_get(self, fields: str = None) -> m.LocaleSettings:
        return await self._build_for_admin_global_settings_locale_settings_get(fields=fields)

    async def admin_global_settings_locale_settings_post(
        self, fields: str = None, locale_settings: m.LocaleSettings = None
    ) -> m.LocaleSettings:
        return await self._build_for_admin_global_settings_locale_settings_post(
            fields=fields, locale_settings=locale_settings
        )

    async def admin_global_settings_notification_settings_get(self, fields: str = None) -> m.NotificationSettings:
        return await self._build_for_admin_global_settings_notification_settings_get(fields=fields)

    async def admin_global_settings_notification_settings_post(
        self, fields: str = None, notification_settings: m.NotificationSettings = None
    ) -> m.NotificationSettings:
        return await self._build_for_admin_global_settings_notification_settings_post(
            fields=fields, notification_settings=notification_settings
        )

    async def admin_global_settings_post(
        self, fields: str = None, global_settings: m.GlobalSettings = None
    ) -> m.GlobalSettings:
        return await self._build_for_admin_global_settings_post(fields=fields, global_settings=global_settings)

    async def admin_global_settings_rest_settings_get(self, fields: str = None) -> m.RestCorsSettings:
        return await self._build_for_admin_global_settings_rest_settings_get(fields=fields)

    async def admin_global_settings_rest_settings_post(
        self, fields: str = None, rest_cors_settings: m.RestCorsSettings = None
    ) -> m.RestCorsSettings:
        return await self._build_for_admin_global_settings_rest_settings_post(
            fields=fields, rest_cors_settings=rest_cors_settings
        )

    async def admin_global_settings_system_settings_get(self, fields: str = None) -> m.SystemSettings:
        return await self._build_for_admin_global_settings_system_settings_get(fields=fields)

    async def admin_global_settings_system_settings_post(
        self, fields: str = None, system_settings: m.SystemSettings = None
    ) -> m.SystemSettings:
        return await self._build_for_admin_global_settings_system_settings_post(
            fields=fields, system_settings=system_settings
        )

    async def admin_projects_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.Project]:
        return await self._build_for_admin_projects_get(fields=fields, skip=skip, top=top)

    async def admin_projects_id_custom_fields_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.ProjectCustomField]:
        return await self._build_for_admin_projects_id_custom_fields_get(id=id, fields=fields, skip=skip, top=top)

    async def admin_projects_id_custom_fields_post(
        self, id: str, fields: str = None, project_custom_field: m.ProjectCustomField = None
    ) -> m.ProjectCustomField:
        return await self._build_for_admin_projects_id_custom_fields_post(
            id=id, fields=fields, project_custom_field=project_custom_field
        )

    async def admin_projects_id_custom_fields_project_custom_field_id_delete(
        self, id: str, project_custom_field_id: str
    ) -> None:
        return await self._build_for_admin_projects_id_custom_fields_project_custom_field_id_delete(
            id=id, project_custom_field_id=project_custom_field_id
        )

    async def admin_projects_id_custom_fields_project_custom_field_id_get(
        self, id: str, project_custom_field_id: str, fields: str = None
    ) -> m.ProjectCustomField:
        return await self._build_for_admin_projects_id_custom_fields_project_custom_field_id_get(
            id=id, project_custom_field_id=project_custom_field_id, fields=fields
        )

    async def admin_projects_id_custom_fields_project_custom_field_id_post(
        self,
        id: str,
        project_custom_field_id: str,
        fields: str = None,
        project_custom_field: m.ProjectCustomField = None,
    ) -> m.ProjectCustomField:
        return await self._build_for_admin_projects_id_custom_fields_project_custom_field_id_post(
            id=id,
            project_custom_field_id=project_custom_field_id,
            fields=fields,
            project_custom_field=project_custom_field,
        )

    async def admin_projects_id_delete(self, id: str) -> None:
        return await self._build_for_admin_projects_id_delete(id=id)

    async def admin_projects_id_get(self, id: str, fields: str = None) -> m.Project:
        return await self._build_for_admin_projects_id_get(id=id, fields=fields)

    async def admin_projects_id_issues_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.Issue]:
        return await self._build_for_admin_projects_id_issues_get(id=id, fields=fields, skip=skip, top=top)

    async def admin_projects_id_issues_issue_id_delete(self, id: str, issue_id: str) -> None:
        return await self._build_for_admin_projects_id_issues_issue_id_delete(id=id, issue_id=issue_id)

    async def admin_projects_id_issues_issue_id_get(self, id: str, issue_id: str, fields: str = None) -> m.Issue:
        return await self._build_for_admin_projects_id_issues_issue_id_get(id=id, issue_id=issue_id, fields=fields)

    async def admin_projects_id_issues_issue_id_post(
        self, id: str, issue_id: str, fields: str = None, issue: m.Issue = None
    ) -> m.Issue:
        return await self._build_for_admin_projects_id_issues_issue_id_post(
            id=id, issue_id=issue_id, fields=fields, issue=issue
        )

    async def admin_projects_id_issues_post(self, id: str, fields: str = None, issue: m.Issue = None) -> m.Issue:
        return await self._build_for_admin_projects_id_issues_post(id=id, fields=fields, issue=issue)

    async def admin_projects_id_post(self, id: str, fields: str = None, project: m.Project = None) -> m.Project:
        return await self._build_for_admin_projects_id_post(id=id, fields=fields, project=project)

    async def admin_projects_id_time_tracking_settings_get(
        self, id: str, fields: str = None
    ) -> m.ProjectTimeTrackingSettings:
        return await self._build_for_admin_projects_id_time_tracking_settings_get(id=id, fields=fields)

    async def admin_projects_id_time_tracking_settings_post(
        self, id: str, fields: str = None, project_time_tracking_settings: m.ProjectTimeTrackingSettings = None
    ) -> m.ProjectTimeTrackingSettings:
        return await self._build_for_admin_projects_id_time_tracking_settings_post(
            id=id, fields=fields, project_time_tracking_settings=project_time_tracking_settings
        )

    async def admin_projects_id_time_tracking_settings_work_item_types_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.WorkItemType]:
        return await self._build_for_admin_projects_id_time_tracking_settings_work_item_types_get(
            id=id, fields=fields, skip=skip, top=top
        )

    async def admin_projects_id_time_tracking_settings_work_item_types_post(
        self, id: str, fields: str = None, work_item_type: m.WorkItemType = None
    ) -> m.WorkItemType:
        return await self._build_for_admin_projects_id_time_tracking_settings_work_item_types_post(
            id=id, fields=fields, work_item_type=work_item_type
        )

    async def admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_delete(
        self, id: str, work_item_type_id: str
    ) -> None:
        return await self._build_for_admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_delete(
            id=id, work_item_type_id=work_item_type_id
        )

    async def admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_get(
        self, id: str, work_item_type_id: str, fields: str = None
    ) -> m.WorkItemType:
        return await self._build_for_admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_get(
            id=id, work_item_type_id=work_item_type_id, fields=fields
        )

    async def admin_projects_post(
        self, template: str = None, fields: str = None, project: m.Project = None
    ) -> m.Project:
        return await self._build_for_admin_projects_post(template=template, fields=fields, project=project)

    async def admin_telemetry_get(self, fields: str = None) -> m.Telemetry:
        return await self._build_for_admin_telemetry_get(fields=fields)

    async def admin_time_tracking_settings_get(self, fields: str = None) -> m.GlobalTimeTrackingSettings:
        return await self._build_for_admin_time_tracking_settings_get(fields=fields)

    async def admin_time_tracking_settings_work_item_types_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.WorkItemType]:
        return await self._build_for_admin_time_tracking_settings_work_item_types_get(fields=fields, skip=skip, top=top)

    async def admin_time_tracking_settings_work_item_types_post(
        self, fields: str = None, work_item_type: m.WorkItemType = None
    ) -> m.WorkItemType:
        return await self._build_for_admin_time_tracking_settings_work_item_types_post(
            fields=fields, work_item_type=work_item_type
        )

    async def admin_time_tracking_settings_work_item_types_work_item_type_id_delete(
        self, work_item_type_id: str
    ) -> None:
        return await self._build_for_admin_time_tracking_settings_work_item_types_work_item_type_id_delete(
            work_item_type_id=work_item_type_id
        )

    async def admin_time_tracking_settings_work_item_types_work_item_type_id_get(
        self, work_item_type_id: str, fields: str = None
    ) -> m.WorkItemType:
        return await self._build_for_admin_time_tracking_settings_work_item_types_work_item_type_id_get(
            work_item_type_id=work_item_type_id, fields=fields
        )

    async def admin_time_tracking_settings_work_item_types_work_item_type_id_post(
        self, work_item_type_id: str, fields: str = None, work_item_type: m.WorkItemType = None
    ) -> m.WorkItemType:
        return await self._build_for_admin_time_tracking_settings_work_item_types_work_item_type_id_post(
            work_item_type_id=work_item_type_id, fields=fields, work_item_type=work_item_type
        )

    async def admin_time_tracking_settings_work_time_settings_get(self, fields: str = None) -> m.WorkTimeSettings:
        return await self._build_for_admin_time_tracking_settings_work_time_settings_get(fields=fields)

    async def admin_time_tracking_settings_work_time_settings_post(
        self, fields: str = None, work_time_settings: m.WorkTimeSettings = None
    ) -> m.WorkTimeSettings:
        return await self._build_for_admin_time_tracking_settings_work_time_settings_post(
            fields=fields, work_time_settings=work_time_settings
        )

    async def agiles_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.Agile]:
        return await self._build_for_agiles_get(fields=fields, skip=skip, top=top)

    async def agiles_id_delete(self, id: str) -> None:
        return await self._build_for_agiles_id_delete(id=id)

    async def agiles_id_get(self, id: str, fields: str = None) -> m.Agile:
        return await self._build_for_agiles_id_get(id=id, fields=fields)

    async def agiles_id_post(self, id: str, fields: str = None, agile: m.Agile = None) -> m.Agile:
        return await self._build_for_agiles_id_post(id=id, fields=fields, agile=agile)

    async def agiles_id_sprints_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.Sprint]:
        return await self._build_for_agiles_id_sprints_get(id=id, fields=fields, skip=skip, top=top)

    async def agiles_id_sprints_post(self, id: str, fields: str = None, sprint: m.Sprint = None) -> m.Sprint:
        return await self._build_for_agiles_id_sprints_post(id=id, fields=fields, sprint=sprint)

    async def agiles_id_sprints_sprint_id_delete(self, id: str, sprint_id: str) -> None:
        return await self._build_for_agiles_id_sprints_sprint_id_delete(id=id, sprint_id=sprint_id)

    async def agiles_id_sprints_sprint_id_get(self, id: str, sprint_id: str, fields: str = None) -> m.Sprint:
        return await self._build_for_agiles_id_sprints_sprint_id_get(id=id, sprint_id=sprint_id, fields=fields)

    async def agiles_id_sprints_sprint_id_post(
        self, id: str, sprint_id: str, fields: str = None, sprint: m.Sprint = None
    ) -> m.Sprint:
        return await self._build_for_agiles_id_sprints_sprint_id_post(
            id=id, sprint_id=sprint_id, fields=fields, sprint=sprint
        )

    async def agiles_post(self, template: str = None, fields: str = None, agile: m.Agile = None) -> m.Agile:
        return await self._build_for_agiles_post(template=template, fields=fields, agile=agile)

    async def groups_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.UserGroup]:
        return await self._build_for_groups_get(fields=fields, skip=skip, top=top)

    async def groups_id_get(self, id: str, fields: str = None) -> m.UserGroup:
        return await self._build_for_groups_id_get(id=id, fields=fields)

    async def issue_link_types_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.IssueLinkType]:
        return await self._build_for_issue_link_types_get(fields=fields, skip=skip, top=top)

    async def issue_link_types_id_delete(self, id: str) -> None:
        return await self._build_for_issue_link_types_id_delete(id=id)

    async def issue_link_types_id_get(self, id: str, fields: str = None) -> m.IssueLinkType:
        return await self._build_for_issue_link_types_id_get(id=id, fields=fields)

    async def issue_link_types_id_post(
        self, id: str, fields: str = None, issue_link_type: m.IssueLinkType = None
    ) -> m.IssueLinkType:
        return await self._build_for_issue_link_types_id_post(id=id, fields=fields, issue_link_type=issue_link_type)

    async def issue_link_types_post(
        self, fields: str = None, issue_link_type: m.IssueLinkType = None
    ) -> m.IssueLinkType:
        return await self._build_for_issue_link_types_post(fields=fields, issue_link_type=issue_link_type)

    async def issue_tags_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.IssueTag]:
        return await self._build_for_issue_tags_get(fields=fields, skip=skip, top=top)

    async def issue_tags_id_delete(self, id: str) -> None:
        return await self._build_for_issue_tags_id_delete(id=id)

    async def issue_tags_id_get(self, id: str, fields: str = None) -> m.IssueTag:
        return await self._build_for_issue_tags_id_get(id=id, fields=fields)

    async def issue_tags_id_issues_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.Issue]:
        return await self._build_for_issue_tags_id_issues_get(id=id, fields=fields, skip=skip, top=top)

    async def issue_tags_id_post(self, id: str, fields: str = None, issue_tag: m.IssueTag = None) -> m.IssueTag:
        return await self._build_for_issue_tags_id_post(id=id, fields=fields, issue_tag=issue_tag)

    async def issue_tags_post(self, fields: str = None, issue_tag: m.IssueTag = None) -> m.IssueTag:
        return await self._build_for_issue_tags_post(fields=fields, issue_tag=issue_tag)

    async def issues_get(
        self, query: str = None, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.Issue]:
        return await self._build_for_issues_get(query=query, fields=fields, skip=skip, top=top)

    async def issues_id_activities_activity_item_id_get(
        self, id: str, activity_item_id: str, fields: str = None
    ) -> m.ActivityItem:
        return await self._build_for_issues_id_activities_activity_item_id_get(
            id=id, activity_item_id=activity_item_id, fields=fields
        )

    async def issues_id_activities_get(
        self,
        id: str,
        categories: str = None,
        reverse: bool = None,
        start: str = None,
        end: str = None,
        author: str = None,
        fields: str = None,
        skip: int = None,
        top: int = None,
    ) -> List[m.ActivityItem]:
        return await self._build_for_issues_id_activities_get(
            id=id,
            categories=categories,
            reverse=reverse,
            start=start,
            end=end,
            author=author,
            fields=fields,
            skip=skip,
            top=top,
        )

    async def issues_id_activities_page_get(
        self,
        id: str,
        categories: str = None,
        reverse: bool = None,
        start: str = None,
        end: str = None,
        author: str = None,
        cursor: str = None,
        activity_id: str = None,
        fields: str = None,
    ) -> m.ActivityCursorPage:
        return await self._build_for_issues_id_activities_page_get(
            id=id,
            categories=categories,
            reverse=reverse,
            start=start,
            end=end,
            author=author,
            cursor=cursor,
            activity_id=activity_id,
            fields=fields,
        )

    async def issues_id_attachments_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.IssueAttachment]:
        return await self._build_for_issues_id_attachments_get(id=id, fields=fields, skip=skip, top=top)

    async def issues_id_attachments_issue_attachment_id_delete(self, id: str, issue_attachment_id: str) -> None:
        return await self._build_for_issues_id_attachments_issue_attachment_id_delete(
            id=id, issue_attachment_id=issue_attachment_id
        )

    async def issues_id_attachments_issue_attachment_id_get(
        self, id: str, issue_attachment_id: str, fields: str = None
    ) -> m.IssueAttachment:
        return await self._build_for_issues_id_attachments_issue_attachment_id_get(
            id=id, issue_attachment_id=issue_attachment_id, fields=fields
        )

    async def issues_id_attachments_issue_attachment_id_post(
        self, id: str, issue_attachment_id: str, fields: str = None, issue_attachment: m.IssueAttachment = None
    ) -> m.IssueAttachment:
        return await self._build_for_issues_id_attachments_issue_attachment_id_post(
            id=id, issue_attachment_id=issue_attachment_id, fields=fields, issue_attachment=issue_attachment
        )

    async def issues_id_attachments_post(
        self, id: str, fields: str = None, issue_attachment: m.IssueAttachment = None
    ) -> m.IssueAttachment:
        return await self._build_for_issues_id_attachments_post(id=id, fields=fields, issue_attachment=issue_attachment)

    async def issues_id_comments_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.IssueComment]:
        return await self._build_for_issues_id_comments_get(id=id, fields=fields, skip=skip, top=top)

    async def issues_id_comments_issue_comment_id_delete(self, id: str, issue_comment_id: str) -> None:
        return await self._build_for_issues_id_comments_issue_comment_id_delete(
            id=id, issue_comment_id=issue_comment_id
        )

    async def issues_id_comments_issue_comment_id_get(
        self, id: str, issue_comment_id: str, fields: str = None
    ) -> m.IssueComment:
        return await self._build_for_issues_id_comments_issue_comment_id_get(
            id=id, issue_comment_id=issue_comment_id, fields=fields
        )

    async def issues_id_comments_issue_comment_id_post(
        self, id: str, issue_comment_id: str, fields: str = None, issue_comment: m.IssueComment = None
    ) -> m.IssueComment:
        return await self._build_for_issues_id_comments_issue_comment_id_post(
            id=id, issue_comment_id=issue_comment_id, fields=fields, issue_comment=issue_comment
        )

    async def issues_id_comments_post(
        self, id: str, draft_id: str = None, fields: str = None, issue_comment: m.IssueComment = None
    ) -> m.IssueComment:
        return await self._build_for_issues_id_comments_post(
            id=id, draft_id=draft_id, fields=fields, issue_comment=issue_comment
        )

    async def issues_id_custom_fields_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.IssueCustomField]:
        return await self._build_for_issues_id_custom_fields_get(id=id, fields=fields, skip=skip, top=top)

    async def issues_id_custom_fields_issue_custom_field_id_get(
        self, id: str, issue_custom_field_id: str, fields: str = None
    ) -> m.IssueCustomField:
        return await self._build_for_issues_id_custom_fields_issue_custom_field_id_get(
            id=id, issue_custom_field_id=issue_custom_field_id, fields=fields
        )

    async def issues_id_custom_fields_issue_custom_field_id_post(
        self, id: str, issue_custom_field_id: str, fields: str = None, issue_custom_field: m.IssueCustomField = None
    ) -> m.IssueCustomField:
        return await self._build_for_issues_id_custom_fields_issue_custom_field_id_post(
            id=id, issue_custom_field_id=issue_custom_field_id, fields=fields, issue_custom_field=issue_custom_field
        )

    async def issues_id_delete(self, id: str) -> None:
        return await self._build_for_issues_id_delete(id=id)

    async def issues_id_get(self, id: str, fields: str = None) -> m.Issue:
        return await self._build_for_issues_id_get(id=id, fields=fields)

    async def issues_id_links_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.IssueLink]:
        return await self._build_for_issues_id_links_get(id=id, fields=fields, skip=skip, top=top)

    async def issues_id_links_issue_link_id_get(self, id: str, issue_link_id: str, fields: str = None) -> m.IssueLink:
        return await self._build_for_issues_id_links_issue_link_id_get(
            id=id, issue_link_id=issue_link_id, fields=fields
        )

    async def issues_id_links_issue_link_id_issues_get(
        self, id: str, issue_link_id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.Issue]:
        return await self._build_for_issues_id_links_issue_link_id_issues_get(
            id=id, issue_link_id=issue_link_id, fields=fields, skip=skip, top=top
        )

    async def issues_id_links_issue_link_id_issues_issue_id_delete(
        self, id: str, issue_link_id: str, issue_id: str
    ) -> None:
        return await self._build_for_issues_id_links_issue_link_id_issues_issue_id_delete(
            id=id, issue_link_id=issue_link_id, issue_id=issue_id
        )

    async def issues_id_links_issue_link_id_issues_post(
        self, id: str, issue_link_id: str, fields: str = None, issue: m.Issue = None
    ) -> m.Issue:
        return await self._build_for_issues_id_links_issue_link_id_issues_post(
            id=id, issue_link_id=issue_link_id, fields=fields, issue=issue
        )

    async def issues_id_post(self, id: str, fields: str = None, issue: m.Issue = None) -> m.Issue:
        return await self._build_for_issues_id_post(id=id, fields=fields, issue=issue)

    async def issues_id_project_get(self, id: str, fields: str = None) -> m.Project:
        return await self._build_for_issues_id_project_get(id=id, fields=fields)

    async def issues_id_project_post(self, id: str, fields: str = None, project: m.Project = None) -> m.Project:
        return await self._build_for_issues_id_project_post(id=id, fields=fields, project=project)

    async def issues_id_time_tracking_get(self, id: str, fields: str = None) -> m.IssueTimeTracker:
        return await self._build_for_issues_id_time_tracking_get(id=id, fields=fields)

    async def issues_id_time_tracking_work_items_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.IssueWorkItem]:
        return await self._build_for_issues_id_time_tracking_work_items_get(id=id, fields=fields, skip=skip, top=top)

    async def issues_id_time_tracking_work_items_issue_work_item_id_delete(
        self, id: str, issue_work_item_id: str
    ) -> None:
        return await self._build_for_issues_id_time_tracking_work_items_issue_work_item_id_delete(
            id=id, issue_work_item_id=issue_work_item_id
        )

    async def issues_id_time_tracking_work_items_issue_work_item_id_get(
        self, id: str, issue_work_item_id: str, fields: str = None
    ) -> m.IssueWorkItem:
        return await self._build_for_issues_id_time_tracking_work_items_issue_work_item_id_get(
            id=id, issue_work_item_id=issue_work_item_id, fields=fields
        )

    async def issues_id_time_tracking_work_items_issue_work_item_id_post(
        self, id: str, issue_work_item_id: str, fields: str = None, issue_work_item: m.IssueWorkItem = None
    ) -> m.IssueWorkItem:
        return await self._build_for_issues_id_time_tracking_work_items_issue_work_item_id_post(
            id=id, issue_work_item_id=issue_work_item_id, fields=fields, issue_work_item=issue_work_item
        )

    async def issues_id_time_tracking_work_items_post(
        self, id: str, fields: str = None, issue_work_item: m.IssueWorkItem = None
    ) -> m.IssueWorkItem:
        return await self._build_for_issues_id_time_tracking_work_items_post(
            id=id, fields=fields, issue_work_item=issue_work_item
        )

    async def issues_post(self, draft_id: str = None, fields: str = None, issue: m.Issue = None) -> m.Issue:
        return await self._build_for_issues_post(draft_id=draft_id, fields=fields, issue=issue)

    async def saved_queries_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.SavedQuery]:
        return await self._build_for_saved_queries_get(fields=fields, skip=skip, top=top)

    async def saved_queries_id_delete(self, id: str) -> None:
        return await self._build_for_saved_queries_id_delete(id=id)

    async def saved_queries_id_get(self, id: str, fields: str = None) -> m.SavedQuery:
        return await self._build_for_saved_queries_id_get(id=id, fields=fields)

    async def saved_queries_id_post(
        self, id: str, fields: str = None, saved_query: m.SavedQuery = None
    ) -> m.SavedQuery:
        return await self._build_for_saved_queries_id_post(id=id, fields=fields, saved_query=saved_query)

    async def saved_queries_post(self, fields: str = None, saved_query: m.SavedQuery = None) -> m.SavedQuery:
        return await self._build_for_saved_queries_post(fields=fields, saved_query=saved_query)

    async def users_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.User]:
        return await self._build_for_users_get(fields=fields, skip=skip, top=top)

    async def users_id_get(self, id: str, fields: str = None) -> m.User:
        return await self._build_for_users_id_get(id=id, fields=fields)

    async def users_id_profiles_general_get(self, id: str, fields: str = None) -> m.GeneralUserProfile:
        return await self._build_for_users_id_profiles_general_get(id=id, fields=fields)

    async def users_id_profiles_general_post(
        self, id: str, fields: str = None, general_user_profile: m.GeneralUserProfile = None
    ) -> m.GeneralUserProfile:
        return await self._build_for_users_id_profiles_general_post(
            id=id, fields=fields, general_user_profile=general_user_profile
        )

    async def users_id_profiles_notifications_get(self, id: str, fields: str = None) -> m.NotificationsUserProfile:
        return await self._build_for_users_id_profiles_notifications_get(id=id, fields=fields)

    async def users_id_profiles_notifications_post(
        self, id: str, fields: str = None, notifications_user_profile: m.NotificationsUserProfile = None
    ) -> m.NotificationsUserProfile:
        return await self._build_for_users_id_profiles_notifications_post(
            id=id, fields=fields, notifications_user_profile=notifications_user_profile
        )

    async def users_id_profiles_timetracking_get(self, id: str, fields: str = None) -> m.TimeTrackingUserProfile:
        return await self._build_for_users_id_profiles_timetracking_get(id=id, fields=fields)

    async def users_id_profiles_timetracking_post(
        self, id: str, fields: str = None, time_tracking_user_profile: m.TimeTrackingUserProfile = None
    ) -> m.TimeTrackingUserProfile:
        return await self._build_for_users_id_profiles_timetracking_post(
            id=id, fields=fields, time_tracking_user_profile=time_tracking_user_profile
        )

    async def users_id_saved_queries_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.SavedQuery]:
        return await self._build_for_users_id_saved_queries_get(id=id, fields=fields, skip=skip, top=top)

    async def users_id_tags_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.IssueTag]:
        return await self._build_for_users_id_tags_get(id=id, fields=fields, skip=skip, top=top)

    async def users_me_get(self, fields: str = None) -> m.Me:
        return await self._build_for_users_me_get(fields=fields)

    async def work_items_get(
        self,
        query: str = None,
        start_date: date = None,
        end_date: date = None,
        start: int = None,
        end: int = None,
        created_start: int = None,
        created_end: int = None,
        updated_start: int = None,
        updated_end: int = None,
        author: str = None,
        creator: str = None,
        fields: str = None,
        skip: int = None,
        top: int = None,
    ) -> List[m.IssueWorkItem]:
        return await self._build_for_work_items_get(
            query=query,
            start_date=start_date,
            end_date=end_date,
            start=start,
            end=end,
            created_start=created_start,
            created_end=created_end,
            updated_start=updated_start,
            updated_end=updated_end,
            author=author,
            creator=creator,
            fields=fields,
            skip=skip,
            top=top,
        )

    async def work_items_id_get(self, id: str, fields: str = None) -> m.IssueWorkItem:
        return await self._build_for_work_items_id_get(id=id, fields=fields)


class SyncDefaultApi(_DefaultApi):
    def activities_get(
        self,
        categories: str = None,
        reverse: bool = None,
        start: str = None,
        end: str = None,
        author: str = None,
        issue_query: str = None,
        fields: str = None,
        skip: int = None,
        top: int = None,
    ) -> List[m.ActivityItem]:
        coroutine = self._build_for_activities_get(
            categories=categories,
            reverse=reverse,
            start=start,
            end=end,
            author=author,
            issue_query=issue_query,
            fields=fields,
            skip=skip,
            top=top,
        )
        return get_event_loop().run_until_complete(coroutine)

    def activities_id_get(self, id: str, fields: str = None) -> m.ActivityItem:
        coroutine = self._build_for_activities_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def activities_page_get(
        self,
        categories: str = None,
        reverse: bool = None,
        start: str = None,
        end: str = None,
        author: str = None,
        issue_query: str = None,
        cursor: str = None,
        activity_id: str = None,
        fields: str = None,
    ) -> m.ActivityCursorPage:
        coroutine = self._build_for_activities_page_get(
            categories=categories,
            reverse=reverse,
            start=start,
            end=end,
            author=author,
            issue_query=issue_query,
            cursor=cursor,
            activity_id=activity_id,
            fields=fields,
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_build_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.BuildBundle]:
        coroutine = self._build_for_admin_custom_field_settings_bundles_build_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_build_id_delete(self, id: str) -> None:
        coroutine = self._build_for_admin_custom_field_settings_bundles_build_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_build_id_get(self, id: str, fields: str = None) -> m.BuildBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_build_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_build_id_post(
        self, id: str, fields: str = None, build_bundle: m.BuildBundle = None
    ) -> m.BuildBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_build_id_post(
            id=id, fields=fields, build_bundle=build_bundle
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_build_post(
        self, fields: str = None, build_bundle: m.BuildBundle = None
    ) -> m.BuildBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_build_post(
            fields=fields, build_bundle=build_bundle
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_enum_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.EnumBundle]:
        coroutine = self._build_for_admin_custom_field_settings_bundles_enum_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_enum_id_delete(self, id: str) -> None:
        coroutine = self._build_for_admin_custom_field_settings_bundles_enum_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_enum_id_get(self, id: str, fields: str = None) -> m.EnumBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_enum_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_enum_id_post(
        self, id: str, fields: str = None, enum_bundle: m.EnumBundle = None
    ) -> m.EnumBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_enum_id_post(
            id=id, fields=fields, enum_bundle=enum_bundle
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_enum_post(
        self, fields: str = None, enum_bundle: m.EnumBundle = None
    ) -> m.EnumBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_enum_post(
            fields=fields, enum_bundle=enum_bundle
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_owned_field_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.OwnedBundle]:
        coroutine = self._build_for_admin_custom_field_settings_bundles_owned_field_get(
            fields=fields, skip=skip, top=top
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_owned_field_id_delete(self, id: str) -> None:
        coroutine = self._build_for_admin_custom_field_settings_bundles_owned_field_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_owned_field_id_get(self, id: str, fields: str = None) -> m.OwnedBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_owned_field_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_owned_field_id_post(
        self, id: str, fields: str = None, owned_bundle: m.OwnedBundle = None
    ) -> m.OwnedBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_owned_field_id_post(
            id=id, fields=fields, owned_bundle=owned_bundle
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_owned_field_post(
        self, fields: str = None, owned_bundle: m.OwnedBundle = None
    ) -> m.OwnedBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_owned_field_post(
            fields=fields, owned_bundle=owned_bundle
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_state_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.StateBundle]:
        coroutine = self._build_for_admin_custom_field_settings_bundles_state_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_state_id_delete(self, id: str) -> None:
        coroutine = self._build_for_admin_custom_field_settings_bundles_state_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_state_id_get(self, id: str, fields: str = None) -> m.StateBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_state_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_state_id_post(
        self, id: str, fields: str = None, state_bundle: m.StateBundle = None
    ) -> m.StateBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_state_id_post(
            id=id, fields=fields, state_bundle=state_bundle
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_state_post(
        self, fields: str = None, state_bundle: m.StateBundle = None
    ) -> m.StateBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_state_post(
            fields=fields, state_bundle=state_bundle
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.UserBundle]:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_id_aggregated_users_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.User]:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_id_aggregated_users_get(
            id=id, fields=fields, skip=skip, top=top
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_id_delete(self, id: str) -> None:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_id_get(self, id: str, fields: str = None) -> m.UserBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_id_groups_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.UserGroup]:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_id_groups_get(
            id=id, fields=fields, skip=skip, top=top
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_id_groups_post(
        self, id: str, fields: str = None, user_group: m.UserGroup = None
    ) -> m.UserGroup:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_id_groups_post(
            id=id, fields=fields, user_group=user_group
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_id_groups_user_group_id_delete(
        self, id: str, user_group_id: str
    ) -> None:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_id_groups_user_group_id_delete(
            id=id, user_group_id=user_group_id
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_id_groups_user_group_id_get(
        self, id: str, user_group_id: str, fields: str = None
    ) -> m.UserGroup:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_id_groups_user_group_id_get(
            id=id, user_group_id=user_group_id, fields=fields
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_id_individuals_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.User]:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_id_individuals_get(
            id=id, fields=fields, skip=skip, top=top
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_id_individuals_post(
        self, id: str, fields: str = None, user: m.User = None
    ) -> m.User:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_id_individuals_post(
            id=id, fields=fields, user=user
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_id_individuals_user_id_delete(self, id: str, user_id: str) -> None:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_id_individuals_user_id_delete(
            id=id, user_id=user_id
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_id_individuals_user_id_get(
        self, id: str, user_id: str, fields: str = None
    ) -> m.User:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_id_individuals_user_id_get(
            id=id, user_id=user_id, fields=fields
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_id_post(
        self, id: str, fields: str = None, user_bundle: m.UserBundle = None
    ) -> m.UserBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_id_post(
            id=id, fields=fields, user_bundle=user_bundle
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_user_post(
        self, fields: str = None, user_bundle: m.UserBundle = None
    ) -> m.UserBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_user_post(
            fields=fields, user_bundle=user_bundle
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_version_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.VersionBundle]:
        coroutine = self._build_for_admin_custom_field_settings_bundles_version_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_version_id_delete(self, id: str) -> None:
        coroutine = self._build_for_admin_custom_field_settings_bundles_version_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_version_id_get(self, id: str, fields: str = None) -> m.VersionBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_version_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_version_id_post(
        self, id: str, fields: str = None, version_bundle: m.VersionBundle = None
    ) -> m.VersionBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_version_id_post(
            id=id, fields=fields, version_bundle=version_bundle
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_bundles_version_post(
        self, fields: str = None, version_bundle: m.VersionBundle = None
    ) -> m.VersionBundle:
        coroutine = self._build_for_admin_custom_field_settings_bundles_version_post(
            fields=fields, version_bundle=version_bundle
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_custom_fields_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.CustomField]:
        coroutine = self._build_for_admin_custom_field_settings_custom_fields_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_custom_fields_id_delete(self, id: str) -> None:
        coroutine = self._build_for_admin_custom_field_settings_custom_fields_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_custom_fields_id_field_defaults_get(
        self, id: str, fields: str = None
    ) -> m.CustomFieldDefaults:
        coroutine = self._build_for_admin_custom_field_settings_custom_fields_id_field_defaults_get(
            id=id, fields=fields
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_custom_fields_id_field_defaults_post(
        self, id: str, fields: str = None, custom_field_defaults: m.CustomFieldDefaults = None
    ) -> m.CustomFieldDefaults:
        coroutine = self._build_for_admin_custom_field_settings_custom_fields_id_field_defaults_post(
            id=id, fields=fields, custom_field_defaults=custom_field_defaults
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_custom_fields_id_get(self, id: str, fields: str = None) -> m.CustomField:
        coroutine = self._build_for_admin_custom_field_settings_custom_fields_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_custom_fields_id_instances_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.ProjectCustomField]:
        coroutine = self._build_for_admin_custom_field_settings_custom_fields_id_instances_get(
            id=id, fields=fields, skip=skip, top=top
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_custom_fields_id_post(
        self, id: str, fields: str = None, custom_field: m.CustomField = None
    ) -> m.CustomField:
        coroutine = self._build_for_admin_custom_field_settings_custom_fields_id_post(
            id=id, fields=fields, custom_field=custom_field
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_custom_fields_post(
        self, fields: str = None, custom_field: m.CustomField = None
    ) -> m.CustomField:
        coroutine = self._build_for_admin_custom_field_settings_custom_fields_post(
            fields=fields, custom_field=custom_field
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_custom_field_settings_types_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.FieldType]:
        coroutine = self._build_for_admin_custom_field_settings_types_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def admin_database_backup_backups_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.BackupFile]:
        coroutine = self._build_for_admin_database_backup_backups_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def admin_database_backup_backups_id_get(self, id: str, fields: str = None) -> m.BackupFile:
        coroutine = self._build_for_admin_database_backup_backups_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_database_backup_settings_backup_status_get(self, fields: str = None) -> m.BackupStatus:
        coroutine = self._build_for_admin_database_backup_settings_backup_status_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_database_backup_settings_get(self, fields: str = None) -> m.DatabaseBackupSettings:
        coroutine = self._build_for_admin_database_backup_settings_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_database_backup_settings_post(
        self, fields: str = None, database_backup_settings: m.DatabaseBackupSettings = None
    ) -> m.DatabaseBackupSettings:
        coroutine = self._build_for_admin_database_backup_settings_post(
            fields=fields, database_backup_settings=database_backup_settings
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_appearance_settings_get(self, fields: str = None) -> m.AppearanceSettings:
        coroutine = self._build_for_admin_global_settings_appearance_settings_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_appearance_settings_post(
        self, fields: str = None, appearance_settings: m.AppearanceSettings = None
    ) -> m.AppearanceSettings:
        coroutine = self._build_for_admin_global_settings_appearance_settings_post(
            fields=fields, appearance_settings=appearance_settings
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_get(self, fields: str = None) -> m.GlobalSettings:
        coroutine = self._build_for_admin_global_settings_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_license_get(self, fields: str = None) -> m.License:
        coroutine = self._build_for_admin_global_settings_license_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_license_post(self, fields: str = None, license: m.License = None) -> m.License:
        coroutine = self._build_for_admin_global_settings_license_post(fields=fields, license=license)
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_locale_settings_get(self, fields: str = None) -> m.LocaleSettings:
        coroutine = self._build_for_admin_global_settings_locale_settings_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_locale_settings_post(
        self, fields: str = None, locale_settings: m.LocaleSettings = None
    ) -> m.LocaleSettings:
        coroutine = self._build_for_admin_global_settings_locale_settings_post(
            fields=fields, locale_settings=locale_settings
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_notification_settings_get(self, fields: str = None) -> m.NotificationSettings:
        coroutine = self._build_for_admin_global_settings_notification_settings_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_notification_settings_post(
        self, fields: str = None, notification_settings: m.NotificationSettings = None
    ) -> m.NotificationSettings:
        coroutine = self._build_for_admin_global_settings_notification_settings_post(
            fields=fields, notification_settings=notification_settings
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_post(
        self, fields: str = None, global_settings: m.GlobalSettings = None
    ) -> m.GlobalSettings:
        coroutine = self._build_for_admin_global_settings_post(fields=fields, global_settings=global_settings)
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_rest_settings_get(self, fields: str = None) -> m.RestCorsSettings:
        coroutine = self._build_for_admin_global_settings_rest_settings_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_rest_settings_post(
        self, fields: str = None, rest_cors_settings: m.RestCorsSettings = None
    ) -> m.RestCorsSettings:
        coroutine = self._build_for_admin_global_settings_rest_settings_post(
            fields=fields, rest_cors_settings=rest_cors_settings
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_system_settings_get(self, fields: str = None) -> m.SystemSettings:
        coroutine = self._build_for_admin_global_settings_system_settings_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_global_settings_system_settings_post(
        self, fields: str = None, system_settings: m.SystemSettings = None
    ) -> m.SystemSettings:
        coroutine = self._build_for_admin_global_settings_system_settings_post(
            fields=fields, system_settings=system_settings
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.Project]:
        coroutine = self._build_for_admin_projects_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_custom_fields_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.ProjectCustomField]:
        coroutine = self._build_for_admin_projects_id_custom_fields_get(id=id, fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_custom_fields_post(
        self, id: str, fields: str = None, project_custom_field: m.ProjectCustomField = None
    ) -> m.ProjectCustomField:
        coroutine = self._build_for_admin_projects_id_custom_fields_post(
            id=id, fields=fields, project_custom_field=project_custom_field
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_custom_fields_project_custom_field_id_delete(
        self, id: str, project_custom_field_id: str
    ) -> None:
        coroutine = self._build_for_admin_projects_id_custom_fields_project_custom_field_id_delete(
            id=id, project_custom_field_id=project_custom_field_id
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_custom_fields_project_custom_field_id_get(
        self, id: str, project_custom_field_id: str, fields: str = None
    ) -> m.ProjectCustomField:
        coroutine = self._build_for_admin_projects_id_custom_fields_project_custom_field_id_get(
            id=id, project_custom_field_id=project_custom_field_id, fields=fields
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_custom_fields_project_custom_field_id_post(
        self,
        id: str,
        project_custom_field_id: str,
        fields: str = None,
        project_custom_field: m.ProjectCustomField = None,
    ) -> m.ProjectCustomField:
        coroutine = self._build_for_admin_projects_id_custom_fields_project_custom_field_id_post(
            id=id,
            project_custom_field_id=project_custom_field_id,
            fields=fields,
            project_custom_field=project_custom_field,
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_delete(self, id: str) -> None:
        coroutine = self._build_for_admin_projects_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_get(self, id: str, fields: str = None) -> m.Project:
        coroutine = self._build_for_admin_projects_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_issues_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.Issue]:
        coroutine = self._build_for_admin_projects_id_issues_get(id=id, fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_issues_issue_id_delete(self, id: str, issue_id: str) -> None:
        coroutine = self._build_for_admin_projects_id_issues_issue_id_delete(id=id, issue_id=issue_id)
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_issues_issue_id_get(self, id: str, issue_id: str, fields: str = None) -> m.Issue:
        coroutine = self._build_for_admin_projects_id_issues_issue_id_get(id=id, issue_id=issue_id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_issues_issue_id_post(
        self, id: str, issue_id: str, fields: str = None, issue: m.Issue = None
    ) -> m.Issue:
        coroutine = self._build_for_admin_projects_id_issues_issue_id_post(
            id=id, issue_id=issue_id, fields=fields, issue=issue
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_issues_post(self, id: str, fields: str = None, issue: m.Issue = None) -> m.Issue:
        coroutine = self._build_for_admin_projects_id_issues_post(id=id, fields=fields, issue=issue)
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_post(self, id: str, fields: str = None, project: m.Project = None) -> m.Project:
        coroutine = self._build_for_admin_projects_id_post(id=id, fields=fields, project=project)
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_time_tracking_settings_get(
        self, id: str, fields: str = None
    ) -> m.ProjectTimeTrackingSettings:
        coroutine = self._build_for_admin_projects_id_time_tracking_settings_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_time_tracking_settings_post(
        self, id: str, fields: str = None, project_time_tracking_settings: m.ProjectTimeTrackingSettings = None
    ) -> m.ProjectTimeTrackingSettings:
        coroutine = self._build_for_admin_projects_id_time_tracking_settings_post(
            id=id, fields=fields, project_time_tracking_settings=project_time_tracking_settings
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_time_tracking_settings_work_item_types_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.WorkItemType]:
        coroutine = self._build_for_admin_projects_id_time_tracking_settings_work_item_types_get(
            id=id, fields=fields, skip=skip, top=top
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_time_tracking_settings_work_item_types_post(
        self, id: str, fields: str = None, work_item_type: m.WorkItemType = None
    ) -> m.WorkItemType:
        coroutine = self._build_for_admin_projects_id_time_tracking_settings_work_item_types_post(
            id=id, fields=fields, work_item_type=work_item_type
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_delete(
        self, id: str, work_item_type_id: str
    ) -> None:
        coroutine = self._build_for_admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_delete(
            id=id, work_item_type_id=work_item_type_id
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_get(
        self, id: str, work_item_type_id: str, fields: str = None
    ) -> m.WorkItemType:
        coroutine = self._build_for_admin_projects_id_time_tracking_settings_work_item_types_work_item_type_id_get(
            id=id, work_item_type_id=work_item_type_id, fields=fields
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_projects_post(self, template: str = None, fields: str = None, project: m.Project = None) -> m.Project:
        coroutine = self._build_for_admin_projects_post(template=template, fields=fields, project=project)
        return get_event_loop().run_until_complete(coroutine)

    def admin_telemetry_get(self, fields: str = None) -> m.Telemetry:
        coroutine = self._build_for_admin_telemetry_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_time_tracking_settings_get(self, fields: str = None) -> m.GlobalTimeTrackingSettings:
        coroutine = self._build_for_admin_time_tracking_settings_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_time_tracking_settings_work_item_types_get(
        self, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.WorkItemType]:
        coroutine = self._build_for_admin_time_tracking_settings_work_item_types_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def admin_time_tracking_settings_work_item_types_post(
        self, fields: str = None, work_item_type: m.WorkItemType = None
    ) -> m.WorkItemType:
        coroutine = self._build_for_admin_time_tracking_settings_work_item_types_post(
            fields=fields, work_item_type=work_item_type
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_time_tracking_settings_work_item_types_work_item_type_id_delete(self, work_item_type_id: str) -> None:
        coroutine = self._build_for_admin_time_tracking_settings_work_item_types_work_item_type_id_delete(
            work_item_type_id=work_item_type_id
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_time_tracking_settings_work_item_types_work_item_type_id_get(
        self, work_item_type_id: str, fields: str = None
    ) -> m.WorkItemType:
        coroutine = self._build_for_admin_time_tracking_settings_work_item_types_work_item_type_id_get(
            work_item_type_id=work_item_type_id, fields=fields
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_time_tracking_settings_work_item_types_work_item_type_id_post(
        self, work_item_type_id: str, fields: str = None, work_item_type: m.WorkItemType = None
    ) -> m.WorkItemType:
        coroutine = self._build_for_admin_time_tracking_settings_work_item_types_work_item_type_id_post(
            work_item_type_id=work_item_type_id, fields=fields, work_item_type=work_item_type
        )
        return get_event_loop().run_until_complete(coroutine)

    def admin_time_tracking_settings_work_time_settings_get(self, fields: str = None) -> m.WorkTimeSettings:
        coroutine = self._build_for_admin_time_tracking_settings_work_time_settings_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def admin_time_tracking_settings_work_time_settings_post(
        self, fields: str = None, work_time_settings: m.WorkTimeSettings = None
    ) -> m.WorkTimeSettings:
        coroutine = self._build_for_admin_time_tracking_settings_work_time_settings_post(
            fields=fields, work_time_settings=work_time_settings
        )
        return get_event_loop().run_until_complete(coroutine)

    def agiles_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.Agile]:
        coroutine = self._build_for_agiles_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def agiles_id_delete(self, id: str) -> None:
        coroutine = self._build_for_agiles_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def agiles_id_get(self, id: str, fields: str = None) -> m.Agile:
        coroutine = self._build_for_agiles_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def agiles_id_post(self, id: str, fields: str = None, agile: m.Agile = None) -> m.Agile:
        coroutine = self._build_for_agiles_id_post(id=id, fields=fields, agile=agile)
        return get_event_loop().run_until_complete(coroutine)

    def agiles_id_sprints_get(self, id: str, fields: str = None, skip: int = None, top: int = None) -> List[m.Sprint]:
        coroutine = self._build_for_agiles_id_sprints_get(id=id, fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def agiles_id_sprints_post(self, id: str, fields: str = None, sprint: m.Sprint = None) -> m.Sprint:
        coroutine = self._build_for_agiles_id_sprints_post(id=id, fields=fields, sprint=sprint)
        return get_event_loop().run_until_complete(coroutine)

    def agiles_id_sprints_sprint_id_delete(self, id: str, sprint_id: str) -> None:
        coroutine = self._build_for_agiles_id_sprints_sprint_id_delete(id=id, sprint_id=sprint_id)
        return get_event_loop().run_until_complete(coroutine)

    def agiles_id_sprints_sprint_id_get(self, id: str, sprint_id: str, fields: str = None) -> m.Sprint:
        coroutine = self._build_for_agiles_id_sprints_sprint_id_get(id=id, sprint_id=sprint_id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def agiles_id_sprints_sprint_id_post(
        self, id: str, sprint_id: str, fields: str = None, sprint: m.Sprint = None
    ) -> m.Sprint:
        coroutine = self._build_for_agiles_id_sprints_sprint_id_post(
            id=id, sprint_id=sprint_id, fields=fields, sprint=sprint
        )
        return get_event_loop().run_until_complete(coroutine)

    def agiles_post(self, template: str = None, fields: str = None, agile: m.Agile = None) -> m.Agile:
        coroutine = self._build_for_agiles_post(template=template, fields=fields, agile=agile)
        return get_event_loop().run_until_complete(coroutine)

    def groups_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.UserGroup]:
        coroutine = self._build_for_groups_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def groups_id_get(self, id: str, fields: str = None) -> m.UserGroup:
        coroutine = self._build_for_groups_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def issue_link_types_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.IssueLinkType]:
        coroutine = self._build_for_issue_link_types_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def issue_link_types_id_delete(self, id: str) -> None:
        coroutine = self._build_for_issue_link_types_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def issue_link_types_id_get(self, id: str, fields: str = None) -> m.IssueLinkType:
        coroutine = self._build_for_issue_link_types_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def issue_link_types_id_post(
        self, id: str, fields: str = None, issue_link_type: m.IssueLinkType = None
    ) -> m.IssueLinkType:
        coroutine = self._build_for_issue_link_types_id_post(id=id, fields=fields, issue_link_type=issue_link_type)
        return get_event_loop().run_until_complete(coroutine)

    def issue_link_types_post(self, fields: str = None, issue_link_type: m.IssueLinkType = None) -> m.IssueLinkType:
        coroutine = self._build_for_issue_link_types_post(fields=fields, issue_link_type=issue_link_type)
        return get_event_loop().run_until_complete(coroutine)

    def issue_tags_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.IssueTag]:
        coroutine = self._build_for_issue_tags_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def issue_tags_id_delete(self, id: str) -> None:
        coroutine = self._build_for_issue_tags_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def issue_tags_id_get(self, id: str, fields: str = None) -> m.IssueTag:
        coroutine = self._build_for_issue_tags_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def issue_tags_id_issues_get(self, id: str, fields: str = None, skip: int = None, top: int = None) -> List[m.Issue]:
        coroutine = self._build_for_issue_tags_id_issues_get(id=id, fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def issue_tags_id_post(self, id: str, fields: str = None, issue_tag: m.IssueTag = None) -> m.IssueTag:
        coroutine = self._build_for_issue_tags_id_post(id=id, fields=fields, issue_tag=issue_tag)
        return get_event_loop().run_until_complete(coroutine)

    def issue_tags_post(self, fields: str = None, issue_tag: m.IssueTag = None) -> m.IssueTag:
        coroutine = self._build_for_issue_tags_post(fields=fields, issue_tag=issue_tag)
        return get_event_loop().run_until_complete(coroutine)

    def issues_get(self, query: str = None, fields: str = None, skip: int = None, top: int = None) -> List[m.Issue]:
        coroutine = self._build_for_issues_get(query=query, fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_activities_activity_item_id_get(
        self, id: str, activity_item_id: str, fields: str = None
    ) -> m.ActivityItem:
        coroutine = self._build_for_issues_id_activities_activity_item_id_get(
            id=id, activity_item_id=activity_item_id, fields=fields
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_activities_get(
        self,
        id: str,
        categories: str = None,
        reverse: bool = None,
        start: str = None,
        end: str = None,
        author: str = None,
        fields: str = None,
        skip: int = None,
        top: int = None,
    ) -> List[m.ActivityItem]:
        coroutine = self._build_for_issues_id_activities_get(
            id=id,
            categories=categories,
            reverse=reverse,
            start=start,
            end=end,
            author=author,
            fields=fields,
            skip=skip,
            top=top,
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_activities_page_get(
        self,
        id: str,
        categories: str = None,
        reverse: bool = None,
        start: str = None,
        end: str = None,
        author: str = None,
        cursor: str = None,
        activity_id: str = None,
        fields: str = None,
    ) -> m.ActivityCursorPage:
        coroutine = self._build_for_issues_id_activities_page_get(
            id=id,
            categories=categories,
            reverse=reverse,
            start=start,
            end=end,
            author=author,
            cursor=cursor,
            activity_id=activity_id,
            fields=fields,
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_attachments_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.IssueAttachment]:
        coroutine = self._build_for_issues_id_attachments_get(id=id, fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_attachments_issue_attachment_id_delete(self, id: str, issue_attachment_id: str) -> None:
        coroutine = self._build_for_issues_id_attachments_issue_attachment_id_delete(
            id=id, issue_attachment_id=issue_attachment_id
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_attachments_issue_attachment_id_get(
        self, id: str, issue_attachment_id: str, fields: str = None
    ) -> m.IssueAttachment:
        coroutine = self._build_for_issues_id_attachments_issue_attachment_id_get(
            id=id, issue_attachment_id=issue_attachment_id, fields=fields
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_attachments_issue_attachment_id_post(
        self, id: str, issue_attachment_id: str, fields: str = None, issue_attachment: m.IssueAttachment = None
    ) -> m.IssueAttachment:
        coroutine = self._build_for_issues_id_attachments_issue_attachment_id_post(
            id=id, issue_attachment_id=issue_attachment_id, fields=fields, issue_attachment=issue_attachment
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_attachments_post(
        self, id: str, fields: str = None, issue_attachment: m.IssueAttachment = None
    ) -> m.IssueAttachment:
        coroutine = self._build_for_issues_id_attachments_post(id=id, fields=fields, issue_attachment=issue_attachment)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_comments_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.IssueComment]:
        coroutine = self._build_for_issues_id_comments_get(id=id, fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_comments_issue_comment_id_delete(self, id: str, issue_comment_id: str) -> None:
        coroutine = self._build_for_issues_id_comments_issue_comment_id_delete(id=id, issue_comment_id=issue_comment_id)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_comments_issue_comment_id_get(
        self, id: str, issue_comment_id: str, fields: str = None
    ) -> m.IssueComment:
        coroutine = self._build_for_issues_id_comments_issue_comment_id_get(
            id=id, issue_comment_id=issue_comment_id, fields=fields
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_comments_issue_comment_id_post(
        self, id: str, issue_comment_id: str, fields: str = None, issue_comment: m.IssueComment = None
    ) -> m.IssueComment:
        coroutine = self._build_for_issues_id_comments_issue_comment_id_post(
            id=id, issue_comment_id=issue_comment_id, fields=fields, issue_comment=issue_comment
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_comments_post(
        self, id: str, draft_id: str = None, fields: str = None, issue_comment: m.IssueComment = None
    ) -> m.IssueComment:
        coroutine = self._build_for_issues_id_comments_post(
            id=id, draft_id=draft_id, fields=fields, issue_comment=issue_comment
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_custom_fields_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.IssueCustomField]:
        coroutine = self._build_for_issues_id_custom_fields_get(id=id, fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_custom_fields_issue_custom_field_id_get(
        self, id: str, issue_custom_field_id: str, fields: str = None
    ) -> m.IssueCustomField:
        coroutine = self._build_for_issues_id_custom_fields_issue_custom_field_id_get(
            id=id, issue_custom_field_id=issue_custom_field_id, fields=fields
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_custom_fields_issue_custom_field_id_post(
        self, id: str, issue_custom_field_id: str, fields: str = None, issue_custom_field: m.IssueCustomField = None
    ) -> m.IssueCustomField:
        coroutine = self._build_for_issues_id_custom_fields_issue_custom_field_id_post(
            id=id, issue_custom_field_id=issue_custom_field_id, fields=fields, issue_custom_field=issue_custom_field
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_delete(self, id: str) -> None:
        coroutine = self._build_for_issues_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_get(self, id: str, fields: str = None) -> m.Issue:
        coroutine = self._build_for_issues_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_links_get(self, id: str, fields: str = None, skip: int = None, top: int = None) -> List[m.IssueLink]:
        coroutine = self._build_for_issues_id_links_get(id=id, fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_links_issue_link_id_get(self, id: str, issue_link_id: str, fields: str = None) -> m.IssueLink:
        coroutine = self._build_for_issues_id_links_issue_link_id_get(id=id, issue_link_id=issue_link_id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_links_issue_link_id_issues_get(
        self, id: str, issue_link_id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.Issue]:
        coroutine = self._build_for_issues_id_links_issue_link_id_issues_get(
            id=id, issue_link_id=issue_link_id, fields=fields, skip=skip, top=top
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_links_issue_link_id_issues_issue_id_delete(self, id: str, issue_link_id: str, issue_id: str) -> None:
        coroutine = self._build_for_issues_id_links_issue_link_id_issues_issue_id_delete(
            id=id, issue_link_id=issue_link_id, issue_id=issue_id
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_links_issue_link_id_issues_post(
        self, id: str, issue_link_id: str, fields: str = None, issue: m.Issue = None
    ) -> m.Issue:
        coroutine = self._build_for_issues_id_links_issue_link_id_issues_post(
            id=id, issue_link_id=issue_link_id, fields=fields, issue=issue
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_post(self, id: str, fields: str = None, issue: m.Issue = None) -> m.Issue:
        coroutine = self._build_for_issues_id_post(id=id, fields=fields, issue=issue)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_project_get(self, id: str, fields: str = None) -> m.Project:
        coroutine = self._build_for_issues_id_project_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_project_post(self, id: str, fields: str = None, project: m.Project = None) -> m.Project:
        coroutine = self._build_for_issues_id_project_post(id=id, fields=fields, project=project)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_time_tracking_get(self, id: str, fields: str = None) -> m.IssueTimeTracker:
        coroutine = self._build_for_issues_id_time_tracking_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_time_tracking_work_items_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.IssueWorkItem]:
        coroutine = self._build_for_issues_id_time_tracking_work_items_get(id=id, fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_time_tracking_work_items_issue_work_item_id_delete(self, id: str, issue_work_item_id: str) -> None:
        coroutine = self._build_for_issues_id_time_tracking_work_items_issue_work_item_id_delete(
            id=id, issue_work_item_id=issue_work_item_id
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_time_tracking_work_items_issue_work_item_id_get(
        self, id: str, issue_work_item_id: str, fields: str = None
    ) -> m.IssueWorkItem:
        coroutine = self._build_for_issues_id_time_tracking_work_items_issue_work_item_id_get(
            id=id, issue_work_item_id=issue_work_item_id, fields=fields
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_time_tracking_work_items_issue_work_item_id_post(
        self, id: str, issue_work_item_id: str, fields: str = None, issue_work_item: m.IssueWorkItem = None
    ) -> m.IssueWorkItem:
        coroutine = self._build_for_issues_id_time_tracking_work_items_issue_work_item_id_post(
            id=id, issue_work_item_id=issue_work_item_id, fields=fields, issue_work_item=issue_work_item
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_id_time_tracking_work_items_post(
        self, id: str, fields: str = None, issue_work_item: m.IssueWorkItem = None
    ) -> m.IssueWorkItem:
        coroutine = self._build_for_issues_id_time_tracking_work_items_post(
            id=id, fields=fields, issue_work_item=issue_work_item
        )
        return get_event_loop().run_until_complete(coroutine)

    def issues_post(self, draft_id: str = None, fields: str = None, issue: m.Issue = None) -> m.Issue:
        coroutine = self._build_for_issues_post(draft_id=draft_id, fields=fields, issue=issue)
        return get_event_loop().run_until_complete(coroutine)

    def saved_queries_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.SavedQuery]:
        coroutine = self._build_for_saved_queries_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def saved_queries_id_delete(self, id: str) -> None:
        coroutine = self._build_for_saved_queries_id_delete(id=id)
        return get_event_loop().run_until_complete(coroutine)

    def saved_queries_id_get(self, id: str, fields: str = None) -> m.SavedQuery:
        coroutine = self._build_for_saved_queries_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def saved_queries_id_post(self, id: str, fields: str = None, saved_query: m.SavedQuery = None) -> m.SavedQuery:
        coroutine = self._build_for_saved_queries_id_post(id=id, fields=fields, saved_query=saved_query)
        return get_event_loop().run_until_complete(coroutine)

    def saved_queries_post(self, fields: str = None, saved_query: m.SavedQuery = None) -> m.SavedQuery:
        coroutine = self._build_for_saved_queries_post(fields=fields, saved_query=saved_query)
        return get_event_loop().run_until_complete(coroutine)

    def users_get(self, fields: str = None, skip: int = None, top: int = None) -> List[m.User]:
        coroutine = self._build_for_users_get(fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def users_id_get(self, id: str, fields: str = None) -> m.User:
        coroutine = self._build_for_users_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def users_id_profiles_general_get(self, id: str, fields: str = None) -> m.GeneralUserProfile:
        coroutine = self._build_for_users_id_profiles_general_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def users_id_profiles_general_post(
        self, id: str, fields: str = None, general_user_profile: m.GeneralUserProfile = None
    ) -> m.GeneralUserProfile:
        coroutine = self._build_for_users_id_profiles_general_post(
            id=id, fields=fields, general_user_profile=general_user_profile
        )
        return get_event_loop().run_until_complete(coroutine)

    def users_id_profiles_notifications_get(self, id: str, fields: str = None) -> m.NotificationsUserProfile:
        coroutine = self._build_for_users_id_profiles_notifications_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def users_id_profiles_notifications_post(
        self, id: str, fields: str = None, notifications_user_profile: m.NotificationsUserProfile = None
    ) -> m.NotificationsUserProfile:
        coroutine = self._build_for_users_id_profiles_notifications_post(
            id=id, fields=fields, notifications_user_profile=notifications_user_profile
        )
        return get_event_loop().run_until_complete(coroutine)

    def users_id_profiles_timetracking_get(self, id: str, fields: str = None) -> m.TimeTrackingUserProfile:
        coroutine = self._build_for_users_id_profiles_timetracking_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def users_id_profiles_timetracking_post(
        self, id: str, fields: str = None, time_tracking_user_profile: m.TimeTrackingUserProfile = None
    ) -> m.TimeTrackingUserProfile:
        coroutine = self._build_for_users_id_profiles_timetracking_post(
            id=id, fields=fields, time_tracking_user_profile=time_tracking_user_profile
        )
        return get_event_loop().run_until_complete(coroutine)

    def users_id_saved_queries_get(
        self, id: str, fields: str = None, skip: int = None, top: int = None
    ) -> List[m.SavedQuery]:
        coroutine = self._build_for_users_id_saved_queries_get(id=id, fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def users_id_tags_get(self, id: str, fields: str = None, skip: int = None, top: int = None) -> List[m.IssueTag]:
        coroutine = self._build_for_users_id_tags_get(id=id, fields=fields, skip=skip, top=top)
        return get_event_loop().run_until_complete(coroutine)

    def users_me_get(self, fields: str = None) -> m.Me:
        coroutine = self._build_for_users_me_get(fields=fields)
        return get_event_loop().run_until_complete(coroutine)

    def work_items_get(
        self,
        query: str = None,
        start_date: date = None,
        end_date: date = None,
        start: int = None,
        end: int = None,
        created_start: int = None,
        created_end: int = None,
        updated_start: int = None,
        updated_end: int = None,
        author: str = None,
        creator: str = None,
        fields: str = None,
        skip: int = None,
        top: int = None,
    ) -> List[m.IssueWorkItem]:
        coroutine = self._build_for_work_items_get(
            query=query,
            start_date=start_date,
            end_date=end_date,
            start=start,
            end=end,
            created_start=created_start,
            created_end=created_end,
            updated_start=updated_start,
            updated_end=updated_end,
            author=author,
            creator=creator,
            fields=fields,
            skip=skip,
            top=top,
        )
        return get_event_loop().run_until_complete(coroutine)

    def work_items_id_get(self, id: str, fields: str = None) -> m.IssueWorkItem:
        coroutine = self._build_for_work_items_id_get(id=id, fields=fields)
        return get_event_loop().run_until_complete(coroutine)
