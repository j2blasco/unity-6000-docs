* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerAttribute-type.html

#  [CustomObjectIndexerAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerAttribute.html).type
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
type; 
### Description
Each time an object of a specific type is indexed, the registered function is called.
```
[CustomObjectIndexer(typeof(Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html)), version = 2)]
internal static void ShaderIndexing(CustomObjectIndexerTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerTarget.html) context, ObjectIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html) indexer)
{
    if (!(context.target is Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader) || !indexer.settings.options.properties)
        return;

    var ownerPropertyType = typeof(Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html));
    for (int i = 0, end = shader.GetPropertyCount(); i != end; ++i)
    {
        var label = shader.GetPropertyName(i);

        // Keep some property name patterns
        if (s_IgnorePropertyNameRx.IsMatch(label))
            continue;

        var name = label.ToLowerInvariant();
        if (name.Length > 0 && name[0] == '_')
            name = name.Substring(1);
        switch (shader.GetPropertyType(i))
        {
            case ShaderPropertyType.Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderPropertyType.Color.html):
                var v = shader.GetPropertyDefaultVectorValue(i);
                IndexColor(name, new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(v.x, v.y, v.z, v.w), indexer, context.documentIndex, label, ownerPropertyType);
                break;
            case ShaderPropertyType.Vector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderPropertyType.Vector.html):
                v = shader.GetPropertyDefaultVectorValue(i);
                IndexVector(name, v, indexer, context.documentIndex, label, ownerPropertyType);
                break;
            case ShaderPropertyType.Float[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderPropertyType.Float.html):
                indexer.IndexNumber(context.documentIndex, name, shader.GetPropertyDefaultFloatValue(i));
                break;
        }
    }
}

```

* * *
