* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.CalculatePlayerSerializationHashForType.html

#  [ContentBuildInterface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.html).CalculatePlayerSerializationHashForType
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
public static [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) CalculatePlayerSerializationHashForType(Type type, [Build.Player.TypeDB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Player.TypeDB.html) typeDB); 
### Parameters
Parameter | Description  
---|---  
type | The type of the object.  
typeDB | The user script TypeDB for the player.  
### Returns
**Hash128** The unique hash for a type's serialized layout. 
### Description
Returns a unique hash for a given type's serialized layout.
Passing in null will provide a hash for the serialized layout of the type as it exists in the editor, passing in a valid [TypeDB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Player.TypeDB.html) for a player will provide a hash for the layout as it exists in the player.  
  
Internal use only. See note on [ContentBuildInterface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.html).
* * *
