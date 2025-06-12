* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.OnActivate.html

#  [AssetSettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html).OnActivate
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
public void OnActivate(string searchContext, [UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) rootElement); 
### Parameters
Parameter | Description  
---|---  
searchContext | Search context in the search box on the Settings window.  
rootElement | Root of the UIElements tree. If you add to this root, the SettingsProvider uses UIElements instead of calling [SettingsProvider.OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.OnGUI.html) to build the UI. If you do not add to this VisualElement, then you must use the IMGUI to build the UI.  
### Description
Overrides [SettingsProvider.OnActivate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.OnActivate.html) for this AssetSettingsProvider.
* * *
