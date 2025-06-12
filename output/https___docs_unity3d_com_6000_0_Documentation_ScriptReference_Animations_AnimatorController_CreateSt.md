* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.CreateStateMachineBehaviour.html

#  [AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html).CreateStateMachineBehaviour
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
public static int CreateStateMachineBehaviour([MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) script); 
### Parameters
Parameter | Description  
---|---  
script | MonoScript class to instantiate.  
### Returns
**int** Returns instance id of created object, returns 0 if something is not valid. 
### Description
This function will create a StateMachineBehaviour instance based on the class define in this script.
This function will validate that the monoscript is a valid statemachine behaviour, the class must be a sub class of StateMachineBehaviour and shouldn't be a generic. Additional resources: [StateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Animations;
using UnityEngine;  
  
public class AddSMB
{
    public void DoAddStateMachineBehaviour(UnityEditor.Animations.AnimatorState state, MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) monoScript)
    {
        if (state == null)
            return;  
  
        int instanceID = AnimatorController.CreateStateMachineBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.CreateStateMachineBehaviour.html)(monoScript);
        if (instanceID == 0)
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Could not create state machine behaviour " + monoScript.name);
            return;
        }  
  
        state.AddStateMachineBehaviour(monoScript.GetClass());  
  
        var obj = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(instanceID);
        if (obj == null)
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("No object could be found with instance id: " + instanceID);
        else
            AssetDatabase.AddObjectToAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AddObjectToAsset.html)(obj, state.ToString());
    }
}

```

* * *
