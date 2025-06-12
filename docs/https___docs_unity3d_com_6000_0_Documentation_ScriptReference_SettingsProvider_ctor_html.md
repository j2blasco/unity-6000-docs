* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-ctor.html

# SettingsProvider Constructor
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
## Declaration
public SettingsProvider(string path, [SettingsScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.html) scopes, IEnumerable<string> keywords); 
### Parameters
Parameter | Description  
---|---  
path | Path of the settings in the Settings window. Uses "/" as separator. The last token becomes the settings label if none is provided.  
scope | Scope of the Settings. The Scope determines where the setting appears: in the Settings or the Preferences windows.  
keywords | List of keywords to compare against what the user is searching for. When the user enters values in the search box on the Settings window, [SettingsProvider.HasSearchInterest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.HasSearchInterest.html) tries to match those keywords to this list.  
### Description
Creates a new SettingsProvider.
```
using System.Collections.Generic;
using System.IO;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;
using UnityEditor.UIElements;  
  
// Create a new type of Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) asset.
class MyCustomSettings : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public const string k_MyCustomSettingsPath = "Assets/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)/MyCustomSettings.asset";  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private int m_Number;  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private string m_SomeString;  
  
    internal static MyCustomSettings GetOrCreateSettings()
    {
        var settings = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<MyCustomSettings>(k_MyCustomSettingsPath);
        if (settings == null)
        {
            settings = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<MyCustomSettings>();
            settings.m_Number = 42;
            settings.m_SomeString = "The answer to the universe";
            AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(settings, k_MyCustomSettingsPath);
            AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();
        }
        return settings;
    }  
  
    internal static SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) GetSerializedSettings()
    {
        return new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(GetOrCreateSettings());
    }
}  
  
// Register a SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) using IMGUI for the drawing framework:
static class MyCustomSettingsIMGUIRegister
{
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateMyCustomSettingsProvider()
    {
        // First parameter is the path in the Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) window.
        // Second parameter is the scope of this setting: it only appears in the Project Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) window.
        var provider = new SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)("Project/MyCustomIMGUISettings", SettingsScope.Project[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.Project.html))
        {
            // By default the last token of the path is used as display name if no label is provided.
            label = "Custom IMGUI",
            // Create the SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) and initialize its drawing (IMGUI) function in place:
            guiHandler = (searchContext) =>
            {
                var settings = MyCustomSettings.GetSerializedSettings();
                EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(settings.FindProperty("m_Number"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("My Number"));
                EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(settings.FindProperty("m_SomeString"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("My String"));
                settings.ApplyModifiedPropertiesWithoutUndo();
            },  
  
            // Populate the search keywords to enable smart search filtering and label highlighting:
            keywords = new HashSet<string>(new[] { "Number", "Some String" })
        };  
  
        return provider;
    }
}  
  
// Register a SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) using UIElements for the drawing framework:
static class MyCustomSettingsUIElementsRegister
{
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateMyCustomSettingsProvider()
    {
        // First parameter is the path in the Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) window.
        // Second parameter is the scope of this setting: it only appears in the Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) window for the Project scope.
        var provider = new SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)("Project/MyCustomUIElementsSettings", SettingsScope.Project[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.Project.html))
        {
            label = "Custom UI Elements",
            // activateHandler is called when the user clicks on the Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) item in the Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) window.
            activateHandler = (searchContext, rootElement) =>
            {
                var settings = MyCustomSettings.GetSerializedSettings();  
  
                // rootElement is a VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html). If you add any children to it, the OnGUI function
                // isn't called because the SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) uses the UIElements drawing framework.
                var styleSheet = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<StyleSheet[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleSheet.html)>("Assets/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)/settings_ui.uss");
                rootElement.styleSheets.Add(styleSheet);
                var title = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)()
                {
                    text = "Custom UI Elements"
                };
                title.AddToClassList("title");
                rootElement.Add(title);  
  
                var properties = new VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)()
                {
                    style =
                    {
                        flexDirection = FlexDirection.Column[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FlexDirection.Column.html)
                    }
                };
                properties.AddToClassList("property-list");
                rootElement.Add(properties);  
  
                properties.Add(new PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.html)(settings.FindProperty("m_SomeString")));
                properties.Add(new PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.html)(settings.FindProperty("m_Number")));  
  
                rootElement.Bind(settings);
            },  
  
            // Populate the search keywords to enable smart search filtering and label highlighting:
            keywords = new HashSet<string>(new[] { "Number", "Some String" })
        };  
  
        return provider;
    }
}  
  
// Create MyCustomSettingsProvider by deriving from SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html):
class MyCustomSettingsProvider : SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)
{
    private SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) m_CustomSettings;  
  
    class Styles
    {
        public static GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) number = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("My Number");
        public static GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) someString = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Some string");
    }  
  
    const string k_MyCustomSettingsPath = "Assets/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)/MyCustomSettings.asset";
    public MyCustomSettingsProvider(string path, SettingsScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.html) scope = SettingsScope.User[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.User.html))
        : base(path, scope) {}  
  
    public static bool IsSettingsAvailable()
    {
        return File.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Exists.html)(k_MyCustomSettingsPath);
    }  
  
    public override void OnActivate(string searchContext, VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) rootElement)
    {
        // This function is called when the user clicks on the MyCustom element in the Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) window.
        m_CustomSettings = MyCustomSettings.GetSerializedSettings();
    }  
  
    public override void OnGUI(string searchContext)
    {
        // Use IMGUI to display UI:
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_CustomSettings.FindProperty("m_Number"), Styles.number);
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_CustomSettings.FindProperty("m_SomeString"), Styles.someString);
        m_CustomSettings.ApplyModifiedPropertiesWithoutUndo();
    }  
  
    // Register the SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateMyCustomSettingsProvider()
    {
        if (IsSettingsAvailable())
        {
            var provider = new MyCustomSettingsProvider("Project/MyCustomSettingsProvider", SettingsScope.Project[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.Project.html));  
  
            // Automatically extract all keywords from the Styles.
            provider.keywords = GetSearchKeywordsFromGUIContentProperties<Styles>();
            return provider;
        }  
  
        // Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) doesn't exist yet; no need to display anything in the Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) window.
        return null;
    }
}

```

* * *
