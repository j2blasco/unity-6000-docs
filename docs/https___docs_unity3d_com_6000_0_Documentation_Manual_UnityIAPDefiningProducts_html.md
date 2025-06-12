* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UnityIAPDefiningProducts.html

  * [Unity Services](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityServices.html)
  * [Unity IAP](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityIAP.html)
  * Cross Platform Guide
  * Defining products


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityIAPCodelessIAP.html)
Codeless IAP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityIAPSubscriptionProducts.html)
Subscription Product support
# Defining products
In order to use in-app purchases, your app must provide a list of Products for sale. You can do this through scripting, or using the [**Codeless IAP Catalog**](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityIAPCodelessIAP.html) (**Window** > **Unity IAP** Abbreviation of Unity **In App Purchase**  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UnityIAP) > **IAP Catalog**). Whichever implementation you use, you must define the appropriate attributes for each Product. This page covers these attributes in detail.
![The IAP Catalog GUI in the Unity Editor](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/IAPCatalogGUI.png) The **IAP Catalog** GUI in the Unity Editor
## Product ID
Enter a cross-platform unique identifier to serve as the Product’s default ID when communicating with an app store. 
**Important** : The ID may only contain lowercase letters, numbers, underscores, or periods.
## Product Type
Each Product must be of one of the following Types:
**Type** | **Description** | **Examples**  
---|---|---  
**Consumable** | Users can purchase the Product repeatedly. Consumable Products cannot be restored. | * Virtual currencies   
* Health potions   
* Temporary power-ups.  
**Non-Consumable** | Users can only purchased the Product once. Non-Consumable Products can be restored. | * Weapons or armor   
* Access to extra content  
**Subscription** | Users can access the Product for a finite period of time. Subscription Products can be restored. | * Monthly access to an online game   
* VIP status granting daily bonuses   
* A free trial  
**Note** : For more information on Subscription type support, see the section on [**Subscription Product support**](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityIAPSubscriptionProducts.html).
## Advanced
This section defines the metadata associated with your Product for use in an in-game store.
### Descriptions
Use the following fields to add descriptive text for your Product:
**Field** | **Data type** | **Description** | **Example**  
---|---|---|---  
**Product Locale** | Enum | Determines the app stores available in your region. |  **English (U.S.)** (Google Play, Apple)  
**Product Title** | String | The name of your Product as it appears in an app store. | “Health Potion”  
**Product Description** | String | The descriptive text for your Product as it appears in an app store, usually an explanation of what the Product is. | “Restores 50 HP.”  
Add **Translations** for the **Title** and **Description** fields by clicking the plus (**+**) icon and selecting an additional locale. You can add as many translations as you like.
![Populating Descriptions fields for Products in the IAP Catalog GUI](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ProductDescription.png) Populating **Descriptions** fields for Products in the **IAP Catalog** GUI
### Payouts
Use this section to add local, fixed definitions for the content you pay out to the purchaser. Payouts make it easier to manage in-game wallets or inventories. By labeling a Product with a name and quantity, developers can quickly adjust in-game counts of certain item types upon purchase (for example, coins or gems).
**Note** : This functionality is only available in Unity 2017.2 or higher. 
**Field** | **Data type** | **Description** | **Example**  
---|---|---|---  
**Payout Type** | Enum | Defines the category of content the purchaser receives. There are four possible Types. | * Currency   
* Item  
* Resource   
* Other  
**Payout Subtype** | String | Provides a level of granularity to the content category. | * “Gold” and “Silver” subtypes of a **Currency** type   
* “Potion” and “Boost” subtypes of an **Item** type  
**Quantity** | Int | Specifies the number of items, currency, and so on, that the purchaser receives in the payout. | * 1   
* >25  
* 100  
**Data** |  | Use this field any way you like as a property to reference in code. | * Flag for a UI element  
* Item rarity  
![Populating Payouts fields for Products in the IAP Catalog GUI](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Payouts.png) Populating **Payouts** fields for Products in the **IAP Catalog** GUI
**Note** : You can add multiple Payouts to a single Product. 
For more information on the PayoutDefinition class, see the [Scripting Reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Purchasing.PayoutDefinition.html). You can always add Payout information to a Product in a script using this class. For example:
```
using UnityEngine.Purchasing;

new PayoutDefinition (PayoutType.Currency, "Gold", 100)

```

Note that the IAP Catalog acts as a Product catalog dictionary, not as an inventory manager. You must still implement the code that handles conveyance of the purchased content. 
### Store ID Overrides
By default, Unity IAP assumes that your Product has the same identifier (specified in the **ID** field, above) across all app stores. Unity recommends doing this where possible. However, there are occasions when this is not possible, such as when publishing to both iOS and Mac stores, which prohibit developers from using the same product ID across both.
In these cases, use the override fields to specify the Product’s correct identifier where it differs from the cross-platform ID.
You can also do this programmatically, as follows:
```
using UnityEngine;
using UnityEngine.Purchasing;

public class MyIAPManager {
    public MyIAPManager () {
        var builder = ConfigurationBuilder.Instance(StandardPurchasingModule.Instance());
        builder.AddProduct("100_gold_coins", ProductType.Consumable, new IDs
        {
            {"100_gold_coins_google", GooglePlay.Name},
            {"100_gold_coins_mac", MacAppStore.Name}
        });
        // Initialize Unity IAP...
    }
}

```

In this example, the Product identifies as “100_gold_coins_google” to Google Play and “100_gold_coins_mac” to the Apple App Store.
**Note** : Overrides only change the identifier Unity IAP uses when communicating with app stores. You should still use the Product’s cross-platform identifier when making API calls.
**Important** : The ID may only contain lowercase letters, numbers, underscores, or periods. 
### Google Configuration (required for Google Play export)
Provide either a Product price, or an ID for a [Pricing Template](https://support.google.com/googleplay/android-developer/answer/6334373) created in Google Play.
![Populating Google Configuration fields for Products in the IAP Catalog GUI.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GoogleConfig.png) Populating **Google Configuration** fields for Products in the **IAP Catalog** GUI.
### Apple Configuration (required for Apple export)
Select a **Pricing Tier** from the dropdown menu. Unity supports predefined Apple price points, but not arbitrary values.
**Select a screenshot** to upload. 
For information on screenshot specs, see Apple’s publisher support documentation.
![Populating Apple Configuration fields for Products in the IAP Catalog GUI.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AppleConfig.png) Populating **Apple Configuration** fields for Products in the **IAP Catalog** GUI.
## Defining Products in scripts
You can also declare your Product list programmatically using the [Purchasing Configuration Builder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Purchasing.ConfigurationBuilder.html). You must provide a unique cross-store **Product ID** and **Product Type** for each Product:
```
using UnityEngine;
using UnityEngine.Purchasing;

public class MyIAPManager {
    public MyIAPManager () {
        var builder = ConfigurationBuilder.Instance(StandardPurchasingModule.Instance());
        builder.AddProduct("100_gold_coins", ProductType.Consumable);
        // Initialize Unity IAP...
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityIAPCodelessIAP.html)
Codeless IAP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityIAPSubscriptionProducts.html)
Subscription Product support
