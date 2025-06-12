* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.ShowObjectPicker.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).ShowObjectPicker
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
public static void ShowObjectPicker([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, bool allowSceneObjects, string searchFilter, int controlID); 
### Parameters
Parameter | Description  
---|---  
obj | The object to be selected by default.  
allowSceneObjects | Is selection of Scene objects allowed, or should it only show assets.  
searchFilter | Default search filter to apply.  
controlID | The id of the control to set. This is useful if you are showing more than one of these. You can get the value at a later time.  
### Description
Show the object picker from code.
Once the user interacts with the Object Picker, it will respond by sending ExecuteCommand events back to the calling OnGUI that called this function. The messages are:  
  
ObjectSelectorUpdated - The selected object was changed. The selected object can be read by calling [GetObjectPickerObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetObjectPickerObject.html) ObjectSelectorClosed - The user closed the object picker.
* * *
