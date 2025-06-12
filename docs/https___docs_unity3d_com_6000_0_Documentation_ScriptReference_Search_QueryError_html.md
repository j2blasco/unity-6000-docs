* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryError.html

# QueryError
class in UnityEditor.Search
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
A QueryError holds the definition of a query parsing error.
QueryErrors are obtained when parsing a query through the function [QueryEngine.Parse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.Parse.html). See [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html) for an example where we recover parsing errors when a query is invalid.
### Properties
Property | Description  
---|---  
[index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryError-index.html) | Index where the error happened.  
[length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryError-length.html) | Length of the block that was being parsed.  
[reason](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryError-reason.html) | Reason why the parsing failed.  
### Constructors
Constructor | Description  
---|---  
[QueryError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryError-ctor.html) | Construct a new QueryError.  
* * *
