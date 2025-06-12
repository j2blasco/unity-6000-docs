* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.GetAdditionalBakedProbes.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.html).GetAdditionalBakedProbes(int id, NativeArray<SphericalHarmonicsL2> outBakedProbeSH, NativeArray<float> outBakedProbeValidity)
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
### Parameters
Parameter | Description  
---|---  
id | The identifier that was used to submit an array of positions to be baked.  
### Returns
**void** True if outBakedProbeSH and outBakedProbeValidity could be successfully returned. 
### Description
Retrieve the bake result of additional probes.
Additional baked probes are probes that can be baked independently of any Light Probe Groups. The baked probe data contains spherical harmonic L2 coefficients as well as a single float value to determine the validity of each probe. By setting an array of probe positions with an identifier, a successive bake will produce probe results for these positions, which can then be fetched again from the API using the identifier.
* * *
