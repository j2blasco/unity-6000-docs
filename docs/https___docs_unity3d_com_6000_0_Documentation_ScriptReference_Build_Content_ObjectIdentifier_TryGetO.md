* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.TryGetObjectIdentifier.html

#  [ObjectIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.html).TryGetObjectIdentifier
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
public static bool TryGetObjectIdentifier([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) targetObject, out [Build.Content.ObjectIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.html) objectId); 
## Declaration
public static bool TryGetObjectIdentifier(int instanceID, out [Build.Content.ObjectIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.html) objectId); 
### Description
Tries to convert a persistent Object into an ObjectIdentifier.
Returns false if it was not possible. This can happen if the Object is is a Scene Object, or was not loaded from and Object on disk.
* * *
