* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.RenderStaticPreview.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).RenderStaticPreview
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
public [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) RenderStaticPreview(string assetPath, Object[] subAssets, int width, int height); 
### Parameters
Parameter | Description  
---|---  
assetPath | The asset to operate on.  
subAssets | An array of all Assets at assetPath.  
width | Width of the created texture.  
height | Height of the created texture.  
### Returns
**Texture2D** Generated texture or null. 
### Description
Override this method if you want to render a static preview.
When overridden [RenderStaticPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.RenderStaticPreview.html) can be used to render a list of assets converted into a single texture. This function will need user supplied source code that can merge the assets together. The size of the create texture can be supplied by the provided width and height.  
If null is returned the builtin icon for the class type is used.
```
// Render the provided asset texture into an Inspector thumbnail.
using UnityEngine;
using System.Collections;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
using System.IO;  
  
public class Example : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) PreviewIcon;
}  
  

[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(Example))]
public class ExampleEditor : UnityEditor.Editor
{
    public static void CreateAsset<Example>() where Example : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
    {
        Example asset = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<Example>();  
  
        string path = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html));  
  
        if (path == "")
        {
            path = "Assets";
        }
        else if (Path.GetExtension(path) != "")
        {
            path = path.Replace(Path.GetFileName(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html))), "");
        }  
  
        string assetPathAndName = AssetDatabase.GenerateUniqueAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GenerateUniqueAssetPath.html)(path + "/New " + typeof(Example).ToString() + ".asset");  
  
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(asset, assetPathAndName);
        AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();
        AssetDatabase.Refresh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Refresh.html)();
        EditorUtility.FocusProjectWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.FocusProjectWindow.html)();
        Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) = asset;
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/RenderStaticPreview example")]
    public static void CreateAsset()
    {
        CreateAsset<Example>();
    }  
  
    public override void OnInspectorGUI()
    {
        Example e = (Example)target;  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();  
  
        // Example has a single arg called PreviewIcon which is a Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)
        e.PreviewIcon = (Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html))
                EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html)(
                    "Thumbnail",                    // string
                    e.PreviewIcon,                  // Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)
                    typeof(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)),              // Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) object, of course
                    false                           // allowSceneObjects
                );  
  
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            EditorUtility.SetDirty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDirty.html)(e);
            AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();
            Repaint();
        }
    }  
  
    public override Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) RenderStaticPreview(string assetPath, Object[] subAssets, int width, int height)
    {
        Example example = (Example)target;  
  
        if (example == null || example.PreviewIcon == null)
            return null;  
  
        // example.PreviewIcon must be a supported format: ARGB32, RGBA32, RGB24,
        // Alpha8 or one of float formats
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) (width, height);
        EditorUtility.CopySerialized[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CopySerialized.html) (example.PreviewIcon, tex);  
  
        return tex;
    }
}
```

* * *
