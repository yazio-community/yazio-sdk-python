"""Contains all the data models used in inputs/outputs"""

from .autoclaim_request import AutoclaimRequest
from .body_value_entry import BodyValueEntry
from .body_value_entry_weight_item import BodyValueEntryWeightItem
from .body_value_update import BodyValueUpdate
from .buddy import Buddy
from .buddy_exercise import BuddyExercise
from .changes_indicator import ChangesIndicator
from .claimables import Claimables
from .consumed_items import ConsumedItems
from .consumed_items_deletion import ConsumedItemsDeletion
from .consumed_items_products_item import ConsumedItemsProductsItem
from .consumed_recipe_portion import ConsumedRecipePortion
from .daily_exercise_summary import DailyExerciseSummary
from .daily_goals import DailyGoals
from .daily_nutrients import DailyNutrients
from .daily_summary_widget import DailySummaryWidget
from .daily_summary_widget_active_fasting_countdown_template_key_type_0 import (
    DailySummaryWidgetActiveFastingCountdownTemplateKeyType0,
)
from .daily_summary_widget_meals import DailySummaryWidgetMeals
from .daily_summary_widget_units import DailySummaryWidgetUnits
from .daily_summary_widget_user import DailySummaryWidgetUser
from .daily_tips_request import DailyTipsRequest
from .daily_tips_request_experiments_item import DailyTipsRequestExperimentsItem
from .dietary_preferences import DietaryPreferences
from .dietary_preferences_restriction_type_0 import DietaryPreferencesRestrictionType0
from .exercise_entry import ExerciseEntry
from .exercise_entry_activity_item import ExerciseEntryActivityItem
from .exercise_log import ExerciseLog
from .exercise_log_activity import ExerciseLogActivity
from .exercise_log_activity_source_type_0 import ExerciseLogActivitySourceType0
from .fasting_participants import FastingParticipants
from .fasting_period_boundary import FastingPeriodBoundary
from .fasting_template import FastingTemplate
from .fasting_template_category import FastingTemplateCategory
from .fasting_template_fasting_periods_item import FastingTemplateFastingPeriodsItem
from .fasting_template_group import FastingTemplateGroup
from .fasting_template_group_fasting_calorie_goal_type_0 import (
    FastingTemplateGroupFastingCalorieGoalType0,
)
from .fasting_template_group_teaser_position_type_0 import FastingTemplateGroupTeaserPositionType0
from .fasting_template_preset_type_0 import FastingTemplatePresetType0
from .fasting_tip import FastingTip
from .feeling import Feeling
from .feeling_note_type_0 import FeelingNoteType0
from .key_value_store import KeyValueStore
from .meal_images import MealImages
from .meal_summary import MealSummary
from .meal_summary_tips import MealSummaryTips
from .meal_summary_tips_request import MealSummaryTipsRequest
from .nutrient_summary import NutrientSummary
from .o_auth_token import OAuthToken
from .o_auth_token_request import OAuthTokenRequest
from .pending_notifications import PendingNotifications
from .product import Product
from .product_nutrients import ProductNutrients
from .product_search_result import ProductSearchResult
from .product_servings_item import ProductServingsItem
from .recipe import Recipe
from .recipe_available_since_type_0 import RecipeAvailableSinceType0
from .recipe_draft import RecipeDraft
from .recipe_draft_nutrients import RecipeDraftNutrients
from .recipe_draft_servings_item import RecipeDraftServingsItem
from .recipe_image_type_0 import RecipeImageType0
from .recipe_index_entry import RecipeIndexEntry
from .recipe_nutrients import RecipeNutrients
from .recipe_servings_item import RecipeServingsItem
from .recipe_servings_item_note_type_0 import RecipeServingsItemNoteType0
from .recipe_servings_item_serving_quantity_type_0 import RecipeServingsItemServingQuantityType0
from .recipe_servings_item_serving_type_0 import RecipeServingsItemServingType0
from .recipe_yazio_id_type_0 import RecipeYazioIdType0
from .shop_items import ShopItems
from .shop_items_items_item import ShopItemsItemsItem
from .streak_calendar import StreakCalendar
from .streak_day import StreakDay
from .streak_update import StreakUpdate
from .subscription import Subscription
from .subscription_base_plan_id_type_0 import SubscriptionBasePlanIdType0
from .suggested_product import SuggestedProduct
from .third_party_integration import ThirdPartyIntegration
from .unlocked_features import UnlockedFeatures
from .unlocked_features_unlocked_features_item import UnlockedFeaturesUnlockedFeaturesItem
from .user_profile import UserProfile
from .user_profile_city_type_0 import UserProfileCityType0
from .user_profile_diet import UserProfileDiet
from .user_profile_last_name_type_0 import UserProfileLastNameType0
from .user_profile_profile_image_type_0 import UserProfileProfileImageType0
from .user_profile_siwa_user_id_type_0 import UserProfileSiwaUserIdType0
from .user_settings import UserSettings
from .wallet import Wallet
from .wallet_currencies_item import WalletCurrenciesItem
from .water_intake import WaterIntake
from .water_intake_entry import WaterIntakeEntry
from .water_intake_gateway_type_0 import WaterIntakeGatewayType0
from .water_intake_source_type_0 import WaterIntakeSourceType0
from .weight_entry import WeightEntry
from .weight_entry_external_id_type_0 import WeightEntryExternalIdType0
from .weight_entry_source_type_0 import WeightEntrySourceType0

__all__ = (
    "AutoclaimRequest",
    "BodyValueEntry",
    "BodyValueEntryWeightItem",
    "BodyValueUpdate",
    "Buddy",
    "BuddyExercise",
    "ChangesIndicator",
    "Claimables",
    "ConsumedItems",
    "ConsumedItemsDeletion",
    "ConsumedItemsProductsItem",
    "ConsumedRecipePortion",
    "DailyExerciseSummary",
    "DailyGoals",
    "DailyNutrients",
    "DailySummaryWidget",
    "DailySummaryWidgetActiveFastingCountdownTemplateKeyType0",
    "DailySummaryWidgetMeals",
    "DailySummaryWidgetUnits",
    "DailySummaryWidgetUser",
    "DailyTipsRequest",
    "DailyTipsRequestExperimentsItem",
    "DietaryPreferences",
    "DietaryPreferencesRestrictionType0",
    "ExerciseEntry",
    "ExerciseEntryActivityItem",
    "ExerciseLog",
    "ExerciseLogActivity",
    "ExerciseLogActivitySourceType0",
    "FastingParticipants",
    "FastingPeriodBoundary",
    "FastingTemplate",
    "FastingTemplateCategory",
    "FastingTemplateFastingPeriodsItem",
    "FastingTemplateGroup",
    "FastingTemplateGroupFastingCalorieGoalType0",
    "FastingTemplateGroupTeaserPositionType0",
    "FastingTemplatePresetType0",
    "FastingTip",
    "Feeling",
    "FeelingNoteType0",
    "KeyValueStore",
    "MealImages",
    "MealSummary",
    "MealSummaryTips",
    "MealSummaryTipsRequest",
    "NutrientSummary",
    "OAuthToken",
    "OAuthTokenRequest",
    "PendingNotifications",
    "Product",
    "ProductNutrients",
    "ProductSearchResult",
    "ProductServingsItem",
    "Recipe",
    "RecipeAvailableSinceType0",
    "RecipeDraft",
    "RecipeDraftNutrients",
    "RecipeDraftServingsItem",
    "RecipeImageType0",
    "RecipeIndexEntry",
    "RecipeNutrients",
    "RecipeServingsItem",
    "RecipeServingsItemNoteType0",
    "RecipeServingsItemServingQuantityType0",
    "RecipeServingsItemServingType0",
    "RecipeYazioIdType0",
    "ShopItems",
    "ShopItemsItemsItem",
    "StreakCalendar",
    "StreakDay",
    "StreakUpdate",
    "Subscription",
    "SubscriptionBasePlanIdType0",
    "SuggestedProduct",
    "ThirdPartyIntegration",
    "UnlockedFeatures",
    "UnlockedFeaturesUnlockedFeaturesItem",
    "UserProfile",
    "UserProfileCityType0",
    "UserProfileDiet",
    "UserProfileLastNameType0",
    "UserProfileProfileImageType0",
    "UserProfileSiwaUserIdType0",
    "UserSettings",
    "Wallet",
    "WalletCurrenciesItem",
    "WaterIntake",
    "WaterIntakeEntry",
    "WaterIntakeGatewayType0",
    "WaterIntakeSourceType0",
    "WeightEntry",
    "WeightEntryExternalIdType0",
    "WeightEntrySourceType0",
)
