* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseElement.AddElementDependencies.html

#  [BaseElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseElement.html).AddElementDependencies
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
public void AddElementDependencies(IEnumerable<uint> elements); 
### Parameters
Parameter | Description  
---|---  
elements | Collection of elements this element will depend on.  
### Description
Adds a list of dependencies by ID to this element.
This element depends on the given elements and therefore will be printed below the specified elements in the generated file.  
  
Unity throws an exception if: 
  * Any of the provided elements do not share the same parent.
  * Any of the provided elements are empty.
  * This element is empty.


* * *
