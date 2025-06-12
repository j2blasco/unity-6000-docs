* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.html

# TextGenerator
class in UnityEngine
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
Class that can be used to generate text for rendering.
Caches vertices, character info, and line info for memory friendlyness.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Font[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.html) font;
    void Start()
    {
        TextGenerationSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerationSettings.html) settings = new TextGenerationSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerationSettings.html)();
        settings.textAnchor = TextAnchor.MiddleCenter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAnchor.MiddleCenter.html);
        settings.color = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
        settings.generationExtents = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(500.0F, 200.0F);
        settings.pivot = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
        settings.richText = true;
        settings.font = font;
        settings.fontSize = 32;
        settings.fontStyle = FontStyle.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FontStyle.Normal.html);
        settings.verticalOverflow = VerticalWrapMode.Overflow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VerticalWrapMode.Overflow.html);
        TextGenerator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.html) generator = new TextGenerator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.html)();
        generator.Populate("I am a string", settings);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("I generated: " + generator.vertexCount + " verts!");
    }
}

```

### Properties
Property | Description  
---|---  
[characterCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator-characterCount.html) | The number of characters that have been generated.  
[characterCountVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator-characterCountVisible.html) | The number of characters that have been generated and are included in the visible lines.  
[characters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator-characters.html) | Array of generated characters.  
[fontSizeUsedForBestFit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator-fontSizeUsedForBestFit.html) | The size of the font that was found if using best fit mode.  
[lineCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator-lineCount.html) | Number of text lines generated.  
[lines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator-lines.html) | Information about each generated text line.  
[rectExtents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator-rectExtents.html) | Extents of the generated text in rect format.  
[vertexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator-vertexCount.html) | Number of vertices generated.  
[verts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator-verts.html) | Array of generated vertices.  
### Constructors
Constructor | Description  
---|---  
[TextGenerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator-ctor.html) | Create a TextGenerator.  
### Public Methods
Method | Description  
---|---  
[GetCharacters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.GetCharacters.html) | Populate the given List with UICharInfo.  
[GetCharactersArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.GetCharactersArray.html) | Returns the current UICharInfo.  
[GetLines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.GetLines.html) | Populate the given list with UILineInfo.  
[GetLinesArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.GetLinesArray.html) | Returns the current UILineInfo.  
[GetPreferredHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.GetPreferredHeight.html) | Given a string and settings, returns the preferred height for a container that would hold this text.  
[GetPreferredWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.GetPreferredWidth.html) | Given a string and settings, returns the preferred width for a container that would hold this text.  
[GetVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.GetVertices.html) | Populate the given list with generated Vertices.  
[GetVerticesArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.GetVerticesArray.html) | Returns the current UIVertex array.  
[Invalidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.Invalidate.html) | Mark the text generator as invalid. This will force a full text generation the next time Populate is called.  
[Populate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.Populate.html) | Will generate the vertices and other data for the given string with the given settings.  
[PopulateWithErrors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextGenerator.PopulateWithErrors.html) | Will generate the vertices and other data for the given string with the given settings.  
* * *
