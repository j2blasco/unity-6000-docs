* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.CollectSources.html

#  [NavMeshBuilder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.html).CollectSources
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
For convenience, you can create a list of build sources directly from the current geometry.
The collection can be controlled in terms of layers, type of geometry and by collecting either by hierarchy or volume.
* * *
## Declaration
public static void CollectSources([Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) includedWorldBounds, int includedLayerMask, [AI.NavMeshCollectGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshCollectGeometry.html) geometry, int defaultArea, List<NavMeshBuildMarkup> markups, List<NavMeshBuildSource> results); 
### Parameters
Parameter | Description  
---|---  
includedWorldBounds | The queried objects must overlap these bounds to be included in the results.  
includedLayerMask | Specifies which layers are included in the query.  
geometry | Which type of geometry to collect - e.g. physics colliders.  
defaultArea | Area type to assign to results, unless modified by NavMeshMarkup.  
markups | List of markups which allows finer control over how objects are collected.  
results | List where results are stored, the list is cleared at the beginning of the call.  
### Description
Collects renderers or physics colliders, and terrains within a volume.
* * *
## Declaration
public static void CollectSources([Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) includedWorldBounds, int includedLayerMask, [AI.NavMeshCollectGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshCollectGeometry.html) geometry, int defaultArea, bool generateLinksByDefault, List<NavMeshBuildMarkup> markups, bool includeOnlyMarkedObjects, List<NavMeshBuildSource> results); 
### Parameters
Parameter | Description  
---|---  
includedWorldBounds | The queried objects must overlap these bounds to be included in the results.  
includedLayerMask | Specifies which layers are included in the query.  
geometry | Which type of geometry to collect - e.g. physics colliders.  
defaultArea | Area type to assign to results, unless modified by NavMeshMarkup.  
generateLinksByDefault | If true, all the source will be considered for generating links. Otherwise, only the marked sources will be considered.  
markups | List of markups which allows finer control over how objects are collected.  
includeOnlyMarkedObjects | Specifies if only objects with markups are collected.  
results | List where results are stored, the list is cleared at the beginning of the call.  
### Description
Collects renderers or physics colliders, and terrains within a volume.
* * *
## Declaration
public static void CollectSources([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) root, int includedLayerMask, [AI.NavMeshCollectGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshCollectGeometry.html) geometry, int defaultArea, List<NavMeshBuildMarkup> markups, List<NavMeshBuildSource> results); 
### Parameters
Parameter | Description  
---|---  
root | If not null, consider only root and its children in the query; if null, includes everything loaded.  
includedLayerMask | Specifies which layers are included in the query.  
geometry | Which type of geometry to collect - e.g. physics colliders.  
defaultArea | Area type to assign to results, unless modified by NavMeshMarkup.  
markups | List of markups which allows finer control over how objects are collected.  
results | List where results are stored, the list is cleared at the beginning of the call.  
### Description
Collects renderers or physics colliders, and terrains within a transform hierarchy.
* * *
## Declaration
public static void CollectSources([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) root, int includedLayerMask, [AI.NavMeshCollectGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshCollectGeometry.html) geometry, int defaultArea, bool generateLinksByDefault, List<NavMeshBuildMarkup> markups, bool includeOnlyMarkedObjects, List<NavMeshBuildSource> results); 
### Parameters
Parameter | Description  
---|---  
root | If not null, consider only root and its children in the query; if null, includes everything loaded.  
includedLayerMask | Specifies which layers are included in the query.  
geometry | Which type of geometry to collect - e.g. physics colliders.  
defaultArea | Area type to assign to results, unless modified by NavMeshMarkup.  
generateLinksByDefault | If true, all the source will be considered for generating links. Otherwise, only the marked sources will be considered.  
markups | List of markups which allows finer control over how objects are collected.  
includeOnlyMarkedObjects | Specifies if only objects with markups are collected.  
results | List where results are stored, the list is cleared at the beginning of the call.  
### Description
Collects renderers or physics colliders, and terrains within a transform hierarchy.
* * *
