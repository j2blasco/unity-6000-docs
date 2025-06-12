* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolAttribute.html

# EditorToolAttribute
class in UnityEditor.EditorTools
/
Inherits from:[EditorTools.ToolAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute.html)
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
Registers an [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) as either a Global tool or a [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) tool for a specific target type.
A Global tool works on any selection. A Global tool is also always available from the top toolbar. A Component tool, like a [CustomEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html), is only available for selections that match a target type.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.EditorTools;
using UnityEngine.Rendering;

// By passing `typeof(MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html))` as the second argument, we register VertexTool as a CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html) tool to be presented
// when the current selection contains a MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) component.
[EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)("Show Vertices", typeof(MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)))]
class VertexTool : EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html), IDrawSelectedHandles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.IDrawSelectedHandles.html)
{
    struct TransformAndPositions
    {
        public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform;
        public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] positions;
    }

    IEnumerable<TransformAndPositions> m_Vertices;
    GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) m_ToolbarIcon;

    public override GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) toolbarIcon
    {
        get
        {
            if (m_ToolbarIcon == null)
                m_ToolbarIcon = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)(
                    AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)>("Assets/Examples/Icons/VertexTool.png"),
                    "Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) Visualization Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html)");
            return m_ToolbarIcon;
        }
    }

    void OnEnable()
    {
        m_Vertices = targets.Select(x =>
        {
            return new TransformAndPositions()
            {
                transform = ((MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html))x).transform,
                positions = ((MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html))x).sharedMesh.vertices
            };
        }).ToArray();
    }

    public override void OnToolGUI(EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window)
    {
        foreach (var entry in m_Vertices)
        {
            var matrix = entry.transform.localToWorldMatrix;
            Drawing.DrawHandleCaps(matrix, entry.positions, Color.cyan[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-cyan.html) * .3f, .05f, CompareFunction.Greater[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CompareFunction.Greater.html));
            Drawing.DrawHandleCaps(matrix, entry.positions, Color.cyan[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-cyan.html), .05f, CompareFunction.LessEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CompareFunction.LessEqual.html));
        }
    }

    public void OnDrawHandles()
    {
        if(!ToolManager.IsActiveTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.IsActiveTool.html)(this))
            return;

        foreach (var entry in m_Vertices)
        {
            var matrix = entry.transform.localToWorldMatrix;
            Drawing.DrawHandleCaps(matrix, entry.positions, Color.cyan[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-cyan.html) * .3f, .03f, CompareFunction.Greater[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CompareFunction.Greater.html));
            Drawing.DrawHandleCaps(matrix, entry.positions, Color.cyan[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-cyan.html), .03f, CompareFunction.LessEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CompareFunction.LessEqual.html));
        }
    }
}

```

You can also use tool variants to group similar tools into a single button in the Tools overlay. Refer to [ToolAttribute.variantGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-variantGroup.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.EditorTools;
using UnityEngine;

namespace GlobalToolVariants
{
    // Define 3 tools that should be shown as a single button in the Tools[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools.html) Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html).
    struct ShapeVariantGroup {}

    [EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)("Line (Custom Global)", variantGroup = typeof(ShapeVariantGroup), variantPriority = 2)]
    [Icon("Assets/Examples/Icons/Variant[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarMenu.Variant.html)-Line.png")]
    class Line : EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) {}

    [EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)("Circle (Custom Global)", variantGroup = typeof(ShapeVariantGroup), variantPriority = 1)]
    [Icon("Assets/Examples/Icons/Variant[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarMenu.Variant.html)-Circle.png")]
    class Circle : EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) {}

    [EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)("Square (Custom Global)", variantGroup = typeof(ShapeVariantGroup), variantPriority = 0)]
    [Icon("Assets/Examples/Icons/Variant[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarMenu.Variant.html)-Square.png")]
    class Square : EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) {}
}

```

### Constructors
Constructor | Description  
---|---  
[EditorToolAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolAttribute-ctor.html) | Registers an EditorTool as either a Global tool or a CustomEditor tool.  
### Inherited Members
### Static Properties
Property | Description  
---|---  
[defaultPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-defaultPriority.html) | The default value for ToolAttribute.toolPriority and ToolAttribute.variantPriority. Specify a priority lower than this value to display a tool before the default entries, or specify a higher value to display it after the default entries.  
### Properties
Property | Description  
---|---  
[displayName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-displayName.html) | The name that displays in menus.  
[targetContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-targetContext.html) | If provided, the EditorTool will only be made available when the ToolManager.activeContextType is equal to targetContext.  
[targetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-targetType.html) | Set to the type that this EditorTool or EditorToolContext can edit. Set to null if the tool is not specific to a Component and should be available at any time.  
[toolPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-toolPriority.html) | Tool priority defines the order that tools are displayed in within the Tools Overlay.  
[variantGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-variantGroup.html) | Tool variants are used to group logically similar tools into a single button in the Tools Overlay.  
[variantPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute-variantPriority.html) | The variant priority defines the order that tools are displayed in when they are displayed in a ToolAttribute.variantGroup dropdown.  
* * *
