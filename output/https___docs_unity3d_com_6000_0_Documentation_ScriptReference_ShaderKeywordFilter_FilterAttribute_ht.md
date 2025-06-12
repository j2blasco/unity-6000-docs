* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.FilterAttribute.html

# FilterAttribute
class in UnityEditor.ShaderKeywordFilter
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
Tell the shader system which shader keywords to include or remove from the build, based on the data field underneath.
This is the base filter attribute class. Use the derived attributes instead: 
  * [SelectIfAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.SelectIfAttribute.html)
  * [SelectIfNotAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.SelectIfNotAttribute.html)
  * [RemoveIfAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.RemoveIfAttribute.html)
  * [RemoveIfNotAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.RemoveIfNotAttribute.html)
  * [SelectOrRemoveAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.SelectOrRemoveAttribute.html)
  * [RemoveOrSelectAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.RemoveOrSelectAttribute.html)


These filter attributes only apply to the build if they're attached to a serialized data field that's part of the type tree of a [RenderPipelineAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html) referenced by [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html). The attributes give you control over which shader keywords Unity uses to build shader variants, based on render pipeline settings.  
  
For example, by default the following shader code generates four different shader variants during the build:
```
#pragma multi_compile __ SHADOWS_LOW SHADOWS_MEDIUM SHADOWS_HIGH
```

If you use filter attributes, this can be adjusted to better suit the settings configuration of the project.   
  
In the following example, when `forceLowShadows` is `true`, the `SelectIf` filter attribute forces the `multi_compile` keyword set to only contain the `SHADOWS_LOW` variant during the build.
```
using UnityEditor.ShaderKeywordFilter;  
  
[SelectIf(true, keywordNames: "SHADOWS_LOW")]
bool forceLowShadows;
```

You can also exclude keywords from the build. In the following example, when `enableHighShadows` is `false`, the `RemoveIf` filter attribute removes `SHADOWS_HIGH`.
```
[RemoveIf(false, keywordNames: "SHADOWS_HIGH")]
bool enableHighShadows;
```

You can also select or remove more than one keyword at a time. In the following example, when `onlyHighOrNoShadows` is `true`, the `SelectIf` filter attribute selects only the `SHADOWS_HIGH` variant and a no shadows variant.  
  
The empty string `""` denotes the empty keyword. You can only select and remove the empty keyword together with another keyword, because `""` on its own applies to all `multi_compile` keyword sets with an empty keyword.
```
[SelectIf(true, keywordNames: new string[] {"", "SHADOWS_HIGH"})]
bool onlyHighOrNoShadows;
```

You can use `RemoveIfNot` with enum data. The following example removes the `SHADOWS_LOW` variant if `shadowMode` is set to anything except `Low`.
```
public enum ShadowMode
{
    Low,
    Med,
    High
}  
  
[RemoveIfNot(ShadowMode.Low, keywordNames: "SHADOWS_LOW")]
ShadowMode shadowMode;
```

You can use the `overridePriority` argument to use filter attributes to override filtering you've previously set. Normally the first filter rule encountered in the type tree targeting a specific keyword takes effect, and Unity ignores any later attributes. If you use `overridePriority`, attributes can force the later filter rule to be active instead.  
  
You can add constraint attributes to filter attributes, to determine whether the filter rule is active in the current context. See [GraphicsAPIConstraintAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.GraphicsAPIConstraintAttribute.html) and [TagConstraintAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.TagConstraintAttribute.html) for more information.
### Constructors
Constructor | Description  
---|---  
[FilterAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.FilterAttribute-ctor.html) | Tell the shader system which shader keywords to include in or exclude from the build, based on the data field underneath.  
* * *
