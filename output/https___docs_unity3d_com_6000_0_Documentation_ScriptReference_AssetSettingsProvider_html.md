* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html

# AssetSettingsProvider
class in UnityEditor
/
Inherits from:[SettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
AssetSettingsProvider is a specialization of the [SettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) class that converts legacy settings to Unified Settings. Legacy settings include any settings that used the Inspector to modify themselves, such as the *.asset files under the ProjectSettings folder. Under the hood, AssetSettingsProvider creates an [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) for specific Assets and builds the UI for the Settings window by wrapping the [Editor.OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html) function.  
  
Internally we use this class to wrap our existing settings.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
// Create a new type of Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html).
class MyCustomSettings : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public const string k_MyCustomSettingsPath = "Assets/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)/MyCustomSettings.asset";  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private int m_Number;  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private string m_SomeString;  
  
    internal static SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) GetSettings()
    {
        var settings = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<MyCustomSettings>(k_MyCustomSettingsPath);
        if (settings == null)
        {
            settings = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<MyCustomSettings>();
            settings.m_Number = 42;
            settings.m_SomeString = "The answer to the universe";
            AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(settings, k_MyCustomSettingsPath);
        }  
  
        return new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(settings);
    }
}  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(MyCustomSettings))]
class MyCustomSettingsEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    // Nothing to do, this uses the Generic Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) to display MyCustomSettings properties
}  
  
class AssetSettingsProviderRegister
{
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateFromFilePath()
    {
        // Create an AssetSettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html) from a file path:
        var provider = AssetSettingsProvider.CreateProviderFromAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.CreateProviderFromAssetPath.html)("Project/AssetSettings/FromFile", MyCustomSettings.k_MyCustomSettingsPath);  
  
        // Register keywords from the properties of MyCustomSettings
        provider.keywords = SettingsProvider.GetSearchKeywordsFromSerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromSerializedObject.html)(new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(AssetDatabase.LoadAllAssetsAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAllAssetsAtPath.html)(MyCustomSettings.k_MyCustomSettingsPath)));
        return provider;
    }  
  
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateFromSettingsObject()
    {
        // Create an AssetSettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html) from a settings object (UnityEngine.Object):
        var settingsObj = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(MyCustomSettings.k_MyCustomSettingsPath);
        var provider = AssetSettingsProvider.CreateProviderFromObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.CreateProviderFromObject.html)("Project/AssetSettings/FromObject", settingsObj);  
  
        // Register keywords from the properties of MyCustomSettings
        provider.keywords = SettingsProvider.GetSearchKeywordsFromSerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromSerializedObject.html)(new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(settingsObj));
        return provider;
    }  
  
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateFromSettingsFromFunctor()
    {
        // Create an AssetSettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html) from a functor that must return a UnityEngine.Object:
        var provider = new AssetSettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html)("Project/AssetSettings/FromFunctor", () => Editor.CreateEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateEditor.html)(AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(MyCustomSettings.k_MyCustomSettingsPath)));  
  
        // Register keywords from the properties of MyCustomSettings
        provider.keywords = SettingsProvider.GetSearchKeywordsFromSerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromSerializedObject.html)(new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(AssetDatabase.LoadAllAssetsAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAllAssetsAtPath.html)(MyCustomSettings.k_MyCustomSettingsPath)));
        return provider;
    }
}

```

### Properties
Property | Description  
---|---  
[settingsEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider-settingsEditor.html) | Editor providing UI to modify the settings.  
### Constructors
Constructor | Description  
---|---  
[AssetSettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider-ctor.html) | Creates a new AssetSettingsProvider so you can wrap legacy settings (that is, settings that previously appeared in the Inspector).  
### Public Methods
Method | Description  
---|---  
[OnActivate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.OnActivate.html) | Overrides SettingsProvider.OnActivate for this AssetSettingsProvider.  
[OnDeactivate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.OnDeactivate.html) | Overrides SettingsProvider.OnDeactivate for this AssetSettingsProvider.  
[OnFooterBarGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.OnFooterBarGUI.html) | Overrides SettingsProvider.OnFooterBarGUI for this AssetSettingsProvider.  
[OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.OnGUI.html) | Overrides SettingsProvider.OnGUI for this AssetSettingsProvider.  
[OnTitleBarGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.OnTitleBarGUI.html) | Overrides SettingsProvider.OnTitleBarGUI for this AssetSettingsProvider. This draws the button bar that contains the "add to preset" and the "help" buttons.  
### Static Methods
Method | Description  
---|---  
[CreateProviderFromAssetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.CreateProviderFromAssetPath.html) | Create an AssetSettingsProvider from an asset path.  
[CreateProviderFromObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.CreateProviderFromObject.html) | Create an AssetSettingsProvider from a settings object.  
[CreateProviderFromResourcePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.CreateProviderFromResourcePath.html) | Create an AssetSettingsProvider from an asset resource path.  
### Inherited Members
### Properties
Property | Description  
---|---  
[activateHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-activateHandler.html) | Overrides SettingsProvider.OnActivate.  
[deactivateHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-deactivateHandler.html) | Overrides SettingsProvider.OnDeactivate.  
[footerBarGuiHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-footerBarGuiHandler.html) | Overrides SettingsProvider.OnFooterBarGUI.  
[guiHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-guiHandler.html) | Overrides SettingsProvider.OnGUI.  
[hasSearchInterestHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-hasSearchInterestHandler.html) | Overrides SettingsProvider.HasSearchInterest.  
[inspectorUpdateHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-inspectorUpdateHandler.html) | Overrides SettingsProvider.OnInspectorUpdate.  
[keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-keywords.html) | Gets or sets the list of keywords to compare against what the user is searching for. When the user enters values in the search box on the Settings window, SettingsProvider.HasSearchInterest tries to match those keywords to this list.  
[label](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-label.html) | Gets or sets the display name of the SettingsProvider as it appears in the Settings window. If not set, the Settings window uses last token of SettingsProvider.settingsPath instead.  
[scope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-scope.html) | Gets the Scope of the SettingsProvider. The Scope determines whether the SettingsProvider appears in the Preferences window (SettingsScope.User) or the Settings window (SettingsScope.Project).  
[settingsPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-settingsPath.html) | Gets Path used to place the SettingsProvider in the tree view of the Settings window. The path should be unique among all other settings paths and should use "/" as its separator.  
[titleBarGuiHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-titleBarGuiHandler.html) | Overrides SettingsProvider.OnTitleBarGUI.  
### Public Methods
Method | Description  
---|---  
[HasSearchInterest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.HasSearchInterest.html) | Checks whether the SettingsProvider should appear when the user types something in the Settings window search box. SettingsProvider tries to match the search terms (even partially) to any of the SettingsProvider.keywords. The search is case insensitive.  
[OnInspectorUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.OnInspectorUpdate.html) | OnInspectorUpdate is called at 10 frames per second to give the inspector a chance to update. See EditorWindow.OnInspectorUpdate for more details.  
[Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.Repaint.html) | Request the SettingsWindow for a repaint.  
### Static Methods
Method | Description  
---|---  
[GetSearchKeywordsFromGUIContentProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromGUIContentProperties.html) | Extract search keywords from all public static memebers in a specific Type.  
[GetSearchKeywordsFromPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromPath.html) | Extract search keywords from the serialized properties of an Asset at a specific path.  
[GetSearchKeywordsFromSerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromSerializedObject.html) | Extract search keywords from from the serialized properties of a SerializedObject.  
* * *
