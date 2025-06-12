* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AIModule.html

# UnityEngine.AIModule
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
The AI module implements the path finding features in Unity.
### Classes
Class | Description  
---|---  
[NavMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMesh.html) | Singleton class to access the baked NavMesh.  
[NavMeshAgent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshAgent.html) | Navigation mesh agent.  
[NavMeshBuilder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.html) | Navigation mesh builder interface.  
[NavMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshData.html) | Contains and represents NavMesh data.  
[NavMeshObstacle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshObstacle.html) | An obstacle for NavMeshAgents to avoid.  
[NavMeshPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshPath.html) | A path as calculated by the navigation system.  
### Structs
Struct | Description  
---|---  
[NavMeshBuildDebugSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildDebugSettings.html) | Specify which of the temporary data generated while building the NavMesh should be retained in memory after the process has completed.  
[NavMeshBuildMarkup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildMarkup.html) | The NavMesh build markup allows you to control how certain objects are treated during the NavMesh build process, specifically when collecting sources for building.  
[NavMeshBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildSettings.html) | The NavMeshBuildSettings struct allows you to specify a collection of settings which describe the dimensions and limitations of a particular agent type.  
[NavMeshBuildSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildSource.html) | The input to the NavMesh builder is a list of NavMesh build sources.  
[NavMeshDataInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshDataInstance.html) | The instance is returned when adding NavMesh data.  
[NavMeshHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshHit.html) | Result information for NavMesh queries.  
[NavMeshLinkData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshLinkData.html) | Used for runtime manipulation of links connecting polygons of the NavMesh.  
[NavMeshLinkInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshLinkInstance.html) | Represents a link available for pathfinding.  
[NavMeshQueryFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshQueryFilter.html) | Specifies which agent type and areas to consider when searching the NavMesh.  
[NavMeshTriangulation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshTriangulation.html) | Contains data describing a triangulation of a navmesh.  
[OffMeshLinkData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.OffMeshLinkData.html) | State of OffMeshLink.  
### Enumerations
Enumeration | Description  
---|---  
[NavMeshBuildDebugFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildDebugFlags.html) | Bitmask used for operating with debug data from the NavMesh build process.  
[NavMeshBuildSourceShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildSourceShape.html) | Used with NavMeshBuildSource to define the shape for building NavMesh.  
[NavMeshCollectGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshCollectGeometry.html) | Used for specifying the type of geometry to collect. Used with NavMeshBuilder.CollectSources.  
[NavMeshObstacleShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshObstacleShape.html) | Shape of the obstacle.  
[NavMeshPathStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshPathStatus.html) | Status of path.  
[ObstacleAvoidanceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.ObstacleAvoidanceType.html) | Level of obstacle avoidance.  
[OffMeshLinkType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.OffMeshLinkType.html) | Link type specifier.  
* * *
