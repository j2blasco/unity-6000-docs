* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.SetAdditionalBakedProbes.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.html).SetAdditionalBakedProbes
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
**Obsolete** Please use UnityEngine.LightTransport.IProbeIntegrator instead.
## Declaration
public static void SetAdditionalBakedProbes(int id, Vector3[] positions); 
**Obsolete** Please use UnityEngine.LightTransport.IProbeIntegrator instead.
## Declaration
public static void SetAdditionalBakedProbes(int id, ReadOnlySpan<Vector3> positions); 
**Obsolete** Please use UnityEngine.LightTransport.IProbeIntegrator instead.
## Declaration
public static void SetAdditionalBakedProbes(int id, ReadOnlySpan<Vector3> positions, bool dering); 
### Parameters
Parameter | Description  
---|---  
id | An ID to identify the positions to be baked. This ID is used later to retrieve the result for those positions.  
positions | An array of probe positions.  
dering | A boolean that determines if Unity should remove ringing from probes.  
### Description
Submit additional probe positions to be baked using an identifier.
Additional baked probes are probes that can be baked independently of any Light Probe Groups. The baked probe data contains spherical harmonic L2 coefficients as well as a single float value to determine the validity of each probe. By setting an array of probe positions with an identifier, a successive bake will produce probe results for these positions, which can then be fetched again from the API using the identifier.
* * *
