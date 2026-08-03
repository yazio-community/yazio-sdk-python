from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_profile_city_type_0 import UserProfileCityType0
    from ..models.user_profile_diet import UserProfileDiet
    from ..models.user_profile_last_name_type_0 import UserProfileLastNameType0
    from ..models.user_profile_profile_image_type_0 import UserProfileProfileImageType0
    from ..models.user_profile_siwa_user_id_type_0 import UserProfileSiwaUserIdType0


T = TypeVar("T", bound="UserProfile")


@_attrs_define
class UserProfile:
    """
    Attributes:
        first_name (str | Unset):
        last_name (None | Unset | UserProfileLastNameType0):
        sex (str | Unset):
        city (None | Unset | UserProfileCityType0):
        country (str | Unset):
        language (str | Unset):
        timezone_offset (float | Unset):
        food_database_country (str | Unset):
        goal (str | Unset):
        activity_degree (str | Unset):
        weight_change_per_week (float | Unset):
        unit_length (str | Unset):
        unit_mass (str | Unset):
        unit_energy (str | Unset):
        unit_glucose (str | Unset):
        unit_serving (str | Unset):
        stripe_customer_id (str | Unset):
        diet (UserProfileDiet | Unset):
        registration_date (str | Unset):
        reset_date (str | Unset):
        profile_image (None | Unset | UserProfileProfileImageType0):
        user_token (str | Unset):
        email_confirmation_status (str | Unset):
        newsletter_opt_in (bool | Unset):
        login_type (str | Unset):
        siwa_user_id (None | Unset | UserProfileSiwaUserIdType0):
        premium_type (str | Unset):
        start_weight (float | Unset):
        uuid (str | Unset):
        body_height (float | Unset):
        date_of_birth (str | Unset):
        email (str | Unset):
        tags (list[Any] | Unset):
    """

    first_name: str | Unset = UNSET
    last_name: None | Unset | UserProfileLastNameType0 = UNSET
    sex: str | Unset = UNSET
    city: None | Unset | UserProfileCityType0 = UNSET
    country: str | Unset = UNSET
    language: str | Unset = UNSET
    timezone_offset: float | Unset = UNSET
    food_database_country: str | Unset = UNSET
    goal: str | Unset = UNSET
    activity_degree: str | Unset = UNSET
    weight_change_per_week: float | Unset = UNSET
    unit_length: str | Unset = UNSET
    unit_mass: str | Unset = UNSET
    unit_energy: str | Unset = UNSET
    unit_glucose: str | Unset = UNSET
    unit_serving: str | Unset = UNSET
    stripe_customer_id: str | Unset = UNSET
    diet: UserProfileDiet | Unset = UNSET
    registration_date: str | Unset = UNSET
    reset_date: str | Unset = UNSET
    profile_image: None | Unset | UserProfileProfileImageType0 = UNSET
    user_token: str | Unset = UNSET
    email_confirmation_status: str | Unset = UNSET
    newsletter_opt_in: bool | Unset = UNSET
    login_type: str | Unset = UNSET
    siwa_user_id: None | Unset | UserProfileSiwaUserIdType0 = UNSET
    premium_type: str | Unset = UNSET
    start_weight: float | Unset = UNSET
    uuid: str | Unset = UNSET
    body_height: float | Unset = UNSET
    date_of_birth: str | Unset = UNSET
    email: str | Unset = UNSET
    tags: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_profile_city_type_0 import UserProfileCityType0
        from ..models.user_profile_last_name_type_0 import UserProfileLastNameType0
        from ..models.user_profile_profile_image_type_0 import UserProfileProfileImageType0
        from ..models.user_profile_siwa_user_id_type_0 import UserProfileSiwaUserIdType0

        first_name = self.first_name

        last_name: dict[str, Any] | None | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        elif isinstance(self.last_name, UserProfileLastNameType0):
            last_name = self.last_name.to_dict()
        else:
            last_name = self.last_name

        sex = self.sex

        city: dict[str, Any] | None | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        elif isinstance(self.city, UserProfileCityType0):
            city = self.city.to_dict()
        else:
            city = self.city

        country = self.country

        language = self.language

        timezone_offset = self.timezone_offset

        food_database_country = self.food_database_country

        goal = self.goal

        activity_degree = self.activity_degree

        weight_change_per_week = self.weight_change_per_week

        unit_length = self.unit_length

        unit_mass = self.unit_mass

        unit_energy = self.unit_energy

        unit_glucose = self.unit_glucose

        unit_serving = self.unit_serving

        stripe_customer_id = self.stripe_customer_id

        diet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diet, Unset):
            diet = self.diet.to_dict()

        registration_date = self.registration_date

        reset_date = self.reset_date

        profile_image: dict[str, Any] | None | Unset
        if isinstance(self.profile_image, Unset):
            profile_image = UNSET
        elif isinstance(self.profile_image, UserProfileProfileImageType0):
            profile_image = self.profile_image.to_dict()
        else:
            profile_image = self.profile_image

        user_token = self.user_token

        email_confirmation_status = self.email_confirmation_status

        newsletter_opt_in = self.newsletter_opt_in

        login_type = self.login_type

        siwa_user_id: dict[str, Any] | None | Unset
        if isinstance(self.siwa_user_id, Unset):
            siwa_user_id = UNSET
        elif isinstance(self.siwa_user_id, UserProfileSiwaUserIdType0):
            siwa_user_id = self.siwa_user_id.to_dict()
        else:
            siwa_user_id = self.siwa_user_id

        premium_type = self.premium_type

        start_weight = self.start_weight

        uuid = self.uuid

        body_height = self.body_height

        date_of_birth = self.date_of_birth

        email = self.email

        tags: list[Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if sex is not UNSET:
            field_dict["sex"] = sex
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if language is not UNSET:
            field_dict["language"] = language
        if timezone_offset is not UNSET:
            field_dict["timezone_offset"] = timezone_offset
        if food_database_country is not UNSET:
            field_dict["food_database_country"] = food_database_country
        if goal is not UNSET:
            field_dict["goal"] = goal
        if activity_degree is not UNSET:
            field_dict["activity_degree"] = activity_degree
        if weight_change_per_week is not UNSET:
            field_dict["weight_change_per_week"] = weight_change_per_week
        if unit_length is not UNSET:
            field_dict["unit_length"] = unit_length
        if unit_mass is not UNSET:
            field_dict["unit_mass"] = unit_mass
        if unit_energy is not UNSET:
            field_dict["unit_energy"] = unit_energy
        if unit_glucose is not UNSET:
            field_dict["unit_glucose"] = unit_glucose
        if unit_serving is not UNSET:
            field_dict["unit_serving"] = unit_serving
        if stripe_customer_id is not UNSET:
            field_dict["stripe_customer_id"] = stripe_customer_id
        if diet is not UNSET:
            field_dict["diet"] = diet
        if registration_date is not UNSET:
            field_dict["registration_date"] = registration_date
        if reset_date is not UNSET:
            field_dict["reset_date"] = reset_date
        if profile_image is not UNSET:
            field_dict["profile_image"] = profile_image
        if user_token is not UNSET:
            field_dict["user_token"] = user_token
        if email_confirmation_status is not UNSET:
            field_dict["email_confirmation_status"] = email_confirmation_status
        if newsletter_opt_in is not UNSET:
            field_dict["newsletter_opt_in"] = newsletter_opt_in
        if login_type is not UNSET:
            field_dict["login_type"] = login_type
        if siwa_user_id is not UNSET:
            field_dict["siwa_user_id"] = siwa_user_id
        if premium_type is not UNSET:
            field_dict["premium_type"] = premium_type
        if start_weight is not UNSET:
            field_dict["start_weight"] = start_weight
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if body_height is not UNSET:
            field_dict["body_height"] = body_height
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if email is not UNSET:
            field_dict["email"] = email
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_profile_city_type_0 import UserProfileCityType0
        from ..models.user_profile_diet import UserProfileDiet
        from ..models.user_profile_last_name_type_0 import UserProfileLastNameType0
        from ..models.user_profile_profile_image_type_0 import UserProfileProfileImageType0
        from ..models.user_profile_siwa_user_id_type_0 import UserProfileSiwaUserIdType0

        d = dict(src_dict)
        first_name = d.pop("first_name", UNSET)

        def _parse_last_name(data: object) -> None | Unset | UserProfileLastNameType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_name_type_0 = UserProfileLastNameType0.from_dict(data)

                return last_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserProfileLastNameType0, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        sex = d.pop("sex", UNSET)

        def _parse_city(data: object) -> None | Unset | UserProfileCityType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                city_type_0 = UserProfileCityType0.from_dict(data)

                return city_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserProfileCityType0, data)

        city = _parse_city(d.pop("city", UNSET))

        country = d.pop("country", UNSET)

        language = d.pop("language", UNSET)

        timezone_offset = d.pop("timezone_offset", UNSET)

        food_database_country = d.pop("food_database_country", UNSET)

        goal = d.pop("goal", UNSET)

        activity_degree = d.pop("activity_degree", UNSET)

        weight_change_per_week = d.pop("weight_change_per_week", UNSET)

        unit_length = d.pop("unit_length", UNSET)

        unit_mass = d.pop("unit_mass", UNSET)

        unit_energy = d.pop("unit_energy", UNSET)

        unit_glucose = d.pop("unit_glucose", UNSET)

        unit_serving = d.pop("unit_serving", UNSET)

        stripe_customer_id = d.pop("stripe_customer_id", UNSET)

        _diet = d.pop("diet", UNSET)
        diet: UserProfileDiet | Unset
        if isinstance(_diet, Unset):
            diet = UNSET
        else:
            diet = UserProfileDiet.from_dict(_diet)

        registration_date = d.pop("registration_date", UNSET)

        reset_date = d.pop("reset_date", UNSET)

        def _parse_profile_image(data: object) -> None | Unset | UserProfileProfileImageType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_image_type_0 = UserProfileProfileImageType0.from_dict(data)

                return profile_image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserProfileProfileImageType0, data)

        profile_image = _parse_profile_image(d.pop("profile_image", UNSET))

        user_token = d.pop("user_token", UNSET)

        email_confirmation_status = d.pop("email_confirmation_status", UNSET)

        newsletter_opt_in = d.pop("newsletter_opt_in", UNSET)

        login_type = d.pop("login_type", UNSET)

        def _parse_siwa_user_id(data: object) -> None | Unset | UserProfileSiwaUserIdType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                siwa_user_id_type_0 = UserProfileSiwaUserIdType0.from_dict(data)

                return siwa_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserProfileSiwaUserIdType0, data)

        siwa_user_id = _parse_siwa_user_id(d.pop("siwa_user_id", UNSET))

        premium_type = d.pop("premium_type", UNSET)

        start_weight = d.pop("start_weight", UNSET)

        uuid = d.pop("uuid", UNSET)

        body_height = d.pop("body_height", UNSET)

        date_of_birth = d.pop("date_of_birth", UNSET)

        email = d.pop("email", UNSET)

        tags = cast(list[Any], d.pop("tags", UNSET))

        user_profile = cls(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            city=city,
            country=country,
            language=language,
            timezone_offset=timezone_offset,
            food_database_country=food_database_country,
            goal=goal,
            activity_degree=activity_degree,
            weight_change_per_week=weight_change_per_week,
            unit_length=unit_length,
            unit_mass=unit_mass,
            unit_energy=unit_energy,
            unit_glucose=unit_glucose,
            unit_serving=unit_serving,
            stripe_customer_id=stripe_customer_id,
            diet=diet,
            registration_date=registration_date,
            reset_date=reset_date,
            profile_image=profile_image,
            user_token=user_token,
            email_confirmation_status=email_confirmation_status,
            newsletter_opt_in=newsletter_opt_in,
            login_type=login_type,
            siwa_user_id=siwa_user_id,
            premium_type=premium_type,
            start_weight=start_weight,
            uuid=uuid,
            body_height=body_height,
            date_of_birth=date_of_birth,
            email=email,
            tags=tags,
        )

        user_profile.additional_properties = d
        return user_profile

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
