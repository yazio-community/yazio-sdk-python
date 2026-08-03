from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buddy_exercise import BuddyExercise
    from ..models.streak_calendar import StreakCalendar


T = TypeVar("T", bound="Buddy")


@_attrs_define
class Buddy:
    """
    Attributes:
        user_uuid (str | Unset):
        name (str | Unset):
        energy_goal (float | Unset):
        protein_goal (float | Unset):
        carb_goal (float | Unset):
        fat_goal (float | Unset):
        consumed_energy (float | Unset):
        consumed_protein (float | Unset):
        consumed_carb (float | Unset):
        consumed_fat (float | Unset):
        water_intake_goal (float | Unset):
        goal (str | Unset):
        start_weight (float | Unset):
        weight_goal (float | Unset):
        weight (float | Unset):
        date_of_birth (str | Unset):
        favorite_recipes (list[str] | Unset):
        exercises (list[BuddyExercise] | Unset):
        sex (str | Unset):
        weight_change_per_week (float | Unset):
        consume_activity_calories (bool | Unset):
        streak (StreakCalendar | Unset):
    """

    user_uuid: str | Unset = UNSET
    name: str | Unset = UNSET
    energy_goal: float | Unset = UNSET
    protein_goal: float | Unset = UNSET
    carb_goal: float | Unset = UNSET
    fat_goal: float | Unset = UNSET
    consumed_energy: float | Unset = UNSET
    consumed_protein: float | Unset = UNSET
    consumed_carb: float | Unset = UNSET
    consumed_fat: float | Unset = UNSET
    water_intake_goal: float | Unset = UNSET
    goal: str | Unset = UNSET
    start_weight: float | Unset = UNSET
    weight_goal: float | Unset = UNSET
    weight: float | Unset = UNSET
    date_of_birth: str | Unset = UNSET
    favorite_recipes: list[str] | Unset = UNSET
    exercises: list[BuddyExercise] | Unset = UNSET
    sex: str | Unset = UNSET
    weight_change_per_week: float | Unset = UNSET
    consume_activity_calories: bool | Unset = UNSET
    streak: StreakCalendar | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_uuid = self.user_uuid

        name = self.name

        energy_goal = self.energy_goal

        protein_goal = self.protein_goal

        carb_goal = self.carb_goal

        fat_goal = self.fat_goal

        consumed_energy = self.consumed_energy

        consumed_protein = self.consumed_protein

        consumed_carb = self.consumed_carb

        consumed_fat = self.consumed_fat

        water_intake_goal = self.water_intake_goal

        goal = self.goal

        start_weight = self.start_weight

        weight_goal = self.weight_goal

        weight = self.weight

        date_of_birth = self.date_of_birth

        favorite_recipes: list[str] | Unset = UNSET
        if not isinstance(self.favorite_recipes, Unset):
            favorite_recipes = self.favorite_recipes

        exercises: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exercises, Unset):
            exercises = []
            for exercises_item_data in self.exercises:
                exercises_item = exercises_item_data.to_dict()
                exercises.append(exercises_item)

        sex = self.sex

        weight_change_per_week = self.weight_change_per_week

        consume_activity_calories = self.consume_activity_calories

        streak: dict[str, Any] | Unset = UNSET
        if not isinstance(self.streak, Unset):
            streak = self.streak.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_uuid is not UNSET:
            field_dict["user_uuid"] = user_uuid
        if name is not UNSET:
            field_dict["name"] = name
        if energy_goal is not UNSET:
            field_dict["energy_goal"] = energy_goal
        if protein_goal is not UNSET:
            field_dict["protein_goal"] = protein_goal
        if carb_goal is not UNSET:
            field_dict["carb_goal"] = carb_goal
        if fat_goal is not UNSET:
            field_dict["fat_goal"] = fat_goal
        if consumed_energy is not UNSET:
            field_dict["consumed_energy"] = consumed_energy
        if consumed_protein is not UNSET:
            field_dict["consumed_protein"] = consumed_protein
        if consumed_carb is not UNSET:
            field_dict["consumed_carb"] = consumed_carb
        if consumed_fat is not UNSET:
            field_dict["consumed_fat"] = consumed_fat
        if water_intake_goal is not UNSET:
            field_dict["water_intake_goal"] = water_intake_goal
        if goal is not UNSET:
            field_dict["goal"] = goal
        if start_weight is not UNSET:
            field_dict["start_weight"] = start_weight
        if weight_goal is not UNSET:
            field_dict["weight_goal"] = weight_goal
        if weight is not UNSET:
            field_dict["weight"] = weight
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if favorite_recipes is not UNSET:
            field_dict["favorite_recipes"] = favorite_recipes
        if exercises is not UNSET:
            field_dict["exercises"] = exercises
        if sex is not UNSET:
            field_dict["sex"] = sex
        if weight_change_per_week is not UNSET:
            field_dict["weight_change_per_week"] = weight_change_per_week
        if consume_activity_calories is not UNSET:
            field_dict["consume_activity_calories"] = consume_activity_calories
        if streak is not UNSET:
            field_dict["streak"] = streak

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.buddy_exercise import BuddyExercise
        from ..models.streak_calendar import StreakCalendar

        d = dict(src_dict)
        user_uuid = d.pop("user_uuid", UNSET)

        name = d.pop("name", UNSET)

        energy_goal = d.pop("energy_goal", UNSET)

        protein_goal = d.pop("protein_goal", UNSET)

        carb_goal = d.pop("carb_goal", UNSET)

        fat_goal = d.pop("fat_goal", UNSET)

        consumed_energy = d.pop("consumed_energy", UNSET)

        consumed_protein = d.pop("consumed_protein", UNSET)

        consumed_carb = d.pop("consumed_carb", UNSET)

        consumed_fat = d.pop("consumed_fat", UNSET)

        water_intake_goal = d.pop("water_intake_goal", UNSET)

        goal = d.pop("goal", UNSET)

        start_weight = d.pop("start_weight", UNSET)

        weight_goal = d.pop("weight_goal", UNSET)

        weight = d.pop("weight", UNSET)

        date_of_birth = d.pop("date_of_birth", UNSET)

        favorite_recipes = cast(list[str], d.pop("favorite_recipes", UNSET))

        _exercises = d.pop("exercises", UNSET)
        exercises: list[BuddyExercise] | Unset = UNSET
        if _exercises is not UNSET:
            exercises = []
            for exercises_item_data in _exercises:
                exercises_item = BuddyExercise.from_dict(exercises_item_data)

                exercises.append(exercises_item)

        sex = d.pop("sex", UNSET)

        weight_change_per_week = d.pop("weight_change_per_week", UNSET)

        consume_activity_calories = d.pop("consume_activity_calories", UNSET)

        _streak = d.pop("streak", UNSET)
        streak: StreakCalendar | Unset
        if isinstance(_streak, Unset):
            streak = UNSET
        else:
            streak = StreakCalendar.from_dict(_streak)

        buddy = cls(
            user_uuid=user_uuid,
            name=name,
            energy_goal=energy_goal,
            protein_goal=protein_goal,
            carb_goal=carb_goal,
            fat_goal=fat_goal,
            consumed_energy=consumed_energy,
            consumed_protein=consumed_protein,
            consumed_carb=consumed_carb,
            consumed_fat=consumed_fat,
            water_intake_goal=water_intake_goal,
            goal=goal,
            start_weight=start_weight,
            weight_goal=weight_goal,
            weight=weight,
            date_of_birth=date_of_birth,
            favorite_recipes=favorite_recipes,
            exercises=exercises,
            sex=sex,
            weight_change_per_week=weight_change_per_week,
            consume_activity_calories=consume_activity_calories,
            streak=streak,
        )

        buddy.additional_properties = d
        return buddy

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
