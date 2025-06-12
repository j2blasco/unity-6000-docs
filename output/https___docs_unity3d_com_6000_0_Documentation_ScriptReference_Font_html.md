* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.html

# Font
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.TextRenderingModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.TextRenderingModule.html)
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
Script interface for [font assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Font.html).
You can use this class to dynamically switch fonts on Text Meshes.  
  
Additional resources: [TextMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html).
### Properties
Property | Description  
---|---  
[ascent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font-ascent.html) | The ascent of the font.  
[characterInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font-characterInfo.html) | Access an array of all characters contained in the font texture.  
[dynamic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font-dynamic.html) | Is the font a dynamic font.  
[fontSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font-fontSize.html) | The default size of the font.  
[lineHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font-lineHeight.html) | The line height of the font.  
[material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font-material.html) | The material used for the font display.  
### Constructors
Constructor | Description  
---|---  
[Font](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font-ctor.html) | Create a new Font.  
### Public Methods
Method | Description  
---|---  
[GetCharacterInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.GetCharacterInfo.html) | Get rendering info for a specific character.  
[HasCharacter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.HasCharacter.html) | Does this font have a specific character?  
[RequestCharactersInTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.RequestCharactersInTexture.html) | Request characters to be added to the font texture (dynamic fonts only).  
### Static Methods
Method | Description  
---|---  
[CreateDynamicFontFromOSFont](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.CreateDynamicFontFromOSFont.html) | Creates a Font object which lets you render a font installed on the user machine.  
[GetMaxVertsForString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.GetMaxVertsForString.html) | Returns the maximum number of verts that the text generator may return for a given string.  
[GetOSInstalledFontNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.GetOSInstalledFontNames.html) | Get names of fonts installed on the machine.  
[GetPathsToOSFonts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.GetPathsToOSFonts.html) | Gets the file paths of the fonts that are installed on the operating system.  
### Events
Event | Description  
---|---  
[textureRebuilt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font-textureRebuilt.html) | Set a function to be called when the dynamic font texture is rebuilt.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
