* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IDataModeController.html

# IDataModeController
interface in UnityEditor
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
Interface with which any [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) can interact with [DataMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DataMode.html) functionalities. To obtain an instance, use [EditorWindow.dataModeController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-dataModeController.html).
This interface displays a switch in the docking area when the window is visible and has more than one supported DataModes.
### Properties
Property | Description  
---|---  
[dataMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IDataModeController-dataMode.html) | Returns the DataMode currently active for the EditorWindow that owns this instance of IDataModeController.  
### Public Methods
Method | Description  
---|---  
[TryChangeDataMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IDataModeController.TryChangeDataMode.html) | Requests a DataMode change for the EditorWindow.  
[UpdateSupportedDataModes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IDataModeController.UpdateSupportedDataModes.html) | Updates the list of DataModes that the EditorWindow supports, and sets the preferred DataMode to use when the DataMode switcher UI is set to Automatic.  
### Events
Event | Description  
---|---  
[dataModeChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IDataModeController-dataModeChanged.html) | Event for subscribing to DataMode changes.  
* * *
