* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddNestedQueryAggregator.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).AddNestedQueryAggregator
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
public void AddNestedQueryAggregator(string token, Func<IEnumerable<TNestedQueryData>,IEnumerable<TNestedQueryData>> aggregator); 
### Parameters
Parameter | Description  
---|---  
token | Name of the aggregator used when typing the query. This name is converted to lowercase when parsing the query to speed up the process.  
aggregator | Aggregator function. Takes the results of the nested query, and returns an aggregate that contains any number of items.  
### Description
Adds a new nested query aggregator. An aggregator is an operation that can be applied on a nested query to aggregate the results of the nested query according to certain criteria.
<typeparam name="TNestedQueryData">The type of data returned by the nested query.</typeparam>
* * *
