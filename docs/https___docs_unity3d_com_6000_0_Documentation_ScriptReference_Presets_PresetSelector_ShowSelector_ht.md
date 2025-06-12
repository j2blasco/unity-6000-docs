* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetSelector.ShowSelector.html

#  [PresetSelector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetSelector.html).ShowSelector
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
public static void ShowSelector(Object[] targets, [Presets.Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) currentSelection, bool createNewAllowed); 
## Declaration
public static void ShowSelector(Object[] targets, [Presets.Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) currentSelection, bool createNewAllowed, Action<Preset> onSelectionChanged, Action<Preset,bool> onSelectionClosed); 
### Parameters
Parameter | Description  
---|---  
targets | The list of objects to which the selected Preset is applied.  
currentSelection | The selected Preset when the window is opened. Set to 'null' for no selection.  
createNewAllowed | Whether to show the 'Create New Preset...' button. Set to true to show the button. Set to false to hide this button.  
onSelectionChanged | Callback invoked when the selected Preset is changed. Provides the selected preset as argument.  
onSelectionClosed | Callback invoked when the PresetSelector window is closed. Provides as arguments the selected preset and whether or not the selction was cancelled.  
### Description
Opens a modal window to select a [Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html).
* * *
## Declaration
public static [Search.ISearchView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html) ShowSelector([Presets.PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html) presetType, [Presets.Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) currentSelection, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) presetProperty, bool createNewAllowed); 
### Parameters
Parameter | Description  
---|---  
presetType | Filters the list of Presets based on a specific [PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html).  
currentSelection | The selected Preset when the window is opened. Set to 'null' for no selection.  
presetProperty | The SerializedProperty behind an ObjectField used to select preset assets.  
createNewAllowed | Whether to show the 'Create New Preset...' button. Set to true to show the button. Set to false to hide this button.  
### Returns
**ISearchView** Returns the search view. 
### Description
Opens a modal window to select a [Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) from an object field backed by a [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).
* * *
**Obsolete** The PresetSelectorReceiver is deprecated. Please use ShowSelector(Object[], Preset, bool).
## Declaration
public static void ShowSelector([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) target, [Presets.Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) currentSelection, bool createNewAllowed, PresetSelectorReceiver eventReceiver); 
**Obsolete** The PresetSelectorReceiver is deprecated. Please use ShowSelector(Object[], Preset, bool).
## Declaration
public static void ShowSelector([Presets.PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html) presetType, [Presets.Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) currentSelection, bool createNewAllowed, PresetSelectorReceiver eventReceiver); 
### Parameters
Parameter | Description  
---|---  
target | Object that identifies the type of Preset asset being selected. The modal window filters the selector view based on this object.  
currentSelection | The selected Preset when the window is opened. Set to 'null' for no selection.  
createNewAllowed | Whether to show the 'Create New Preset...' button. Set to true to show the button. Set to false to hide this button.  
eventReceiver | The PresetSelectorReceiver instance that the PresetSelector uses to send events.  
presetType | Filters the list of Presets based on a specific PresetType. Use this param to set the PresetType when no target is specified.  
### Description
OBSOLETE. Opens a modal window to select a [Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html).
* * *
