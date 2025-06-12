* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-ctor.html

# TextAsset Constructor
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextAsset.html "Go to TextAsset Component in the Manual")
## Declaration
public TextAsset(string text); 
### Parameters
Parameter | Description  
---|---  
text | The text contents for the [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html).  
### Description
Creates a new [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) with specified text contents.
This constructor creates a [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html), not a plain text file. To save a [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) to disk using the [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html) class, save the [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) with the .asset extension.
* * *
## Declaration
public TextAsset(ReadOnlySpan<byte> bytes); 
### Parameters
Parameter | Description  
---|---  
bytes | The byte contents for the [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html).  
### Description
Creates a new [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) with specified byte contents.
This constructor creates a [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html), not a plain text file. To save a [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) to disk using the [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html) class, save the [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) with the .asset extension.  
  
Use this form of the constructor to specify an arbitrary byte buffer to store in the TextAsset. Use the [TextAsset.bytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-bytes.html) property to access this data or use the [TextAsset.text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-text.html) property to interpret the byte data as text.
* * *
