* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextMesh.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Text meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/text-meshes.html)
  * Text Mesh component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-meshes-text-strings.html)
Create meshes for text strings
[](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-components-reference.html)
Mesh components reference
# Text Mesh component reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html "Go to TextMesh page in the Scripting Reference")
The **Text**Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh)** component generates 3D geometry that displays text strings.
**Note:** The **Text Mesh** component has limited functionality. For information on more recent, full-featured ways of displaying text, see [Creating user interfaces (UI)](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html).
To create a new Text Mesh, go to **Component > Mesh > Text Mesh**.
## Text Mesh properties
**_Property:_** | **_Function:_**  
---|---  
**Text** | The text that will be rendered  
**Offset Z** | How far should the text be offset from the transform.position.z when drawing  
**Character Size** | The size of each character (This scales the whole text.)  
**Line Spacing** | How much space will be in-between lines of text.  
**Anchor** | Which point of the text shares the position of the Transform.  
**Alignment** | How lines of text are aligned (Left, Right, Center).  
**Tab Size** | How much space will be inserted for a tab ‘\t’ character. This is a multiplum of the ‘spacebar’ character offset.  
**Font Size** | The size of the font. This can override the size of a dynamic font.  
**Font Style** | The rendering style of the font. The font needs to be marked as dynamic.  
**Rich Text** | When selected this will enable tag processing when the text is rendered.  
**Font** | The [TrueType Font](https://docs.unity3d.com/6000.0/Documentation/Manual/create-meshes-text-strings.html) to use when rendering the text.  
**Color** | The global color to use when rendering the text.  
TextMesh
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-meshes-text-strings.html)
Create meshes for text strings
[](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-components-reference.html)
Mesh components reference
