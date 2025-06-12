* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html

# QueryEngine
class in UnityEditor.Search
/
Inherits from:[Search.QueryEngine_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html)
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
A QueryEngine defines how to build a query from an input string. It can be customized to support custom filters and operators. Default query engine of type object.
See [QueryEngine<T>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).
### Constructors
Constructor | Description  
---|---  
[QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine-ctor.html) | Construct a new QueryEngine.  
### Inherited Members
### Properties
Property | Description  
---|---  
[globalStringComparison](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-globalStringComparison.html) | Global string comparison options for word matching and filter handling (if not overridden).  
[searchDataCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-searchDataCallback.html) | The callback used to get the data to match to the search words.  
[searchDataOverridesStringComparison](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-searchDataOverridesStringComparison.html) | Indicates if word/phrase matching uses searchDataStringComparison or not.  
[searchDataStringComparison](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-searchDataStringComparison.html) | String comparison options for word/phrase matching.  
[searchWordMatcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-searchWordMatcher.html) | The function used to match the search data against the search words.  
[skipIncompleteFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-skipIncompleteFilters.html) | Boolean. Indicates if incomplete filters should be skipped. If true, filters are skipped. If false and validateFilters is true, incomplete filters will generate errors when parsed.  
[skipUnknownFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-skipUnknownFilters.html) | Boolean. Indicates if unknown filters should be skipped. If true, unknown filters are skipped. If false and validateFilters is true, unknown filters will generate errors if no default filter handler is provided.  
[validateFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-validateFilters.html) | Get or set if the engine must validate filters when parsing the query. Defaults to true.  
### Public Methods
Method | Description  
---|---  
[AddFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddFilter.html) | Adds a new custom filter.  
[AddFiltersFromAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddFiltersFromAttribute.html) | Adds all custom filters that are identified with the method attribute TFilterAttribute.  
[AddNestedQueryAggregator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddNestedQueryAggregator.html) | Adds a new nested query aggregator. An aggregator is an operation that can be applied on a nested query to aggregate the results of the nested query according to certain criteria.  
[AddOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddOperator.html) | Adds a custom filter operator.  
[AddOperatorHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddOperatorHandler.html) | Adds a custom filter operator handler.  
[AddTypeParser](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddTypeParser.html) | Adds a type parser that parses a string and returns a custom type. Used by custom operator handlers (see AddOperatorHandler).  
[ClearFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.ClearFilters.html) | Removes all filters that were added on the QueryEngine.  
[GetAllFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.GetAllFilters.html) | Get all filters added on this QueryEngine.  
[GetOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.GetOperator.html) | Get a custom operator added on the QueryEngine.  
[ParseQuery](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.ParseQuery.html) | Parses a query string into a ParsedQuery operation. This ParsedQuery operation can then be used to filter any data set of type TData.  
[RemoveFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.RemoveFilter.html) | Removes a custom filter.  
[RemoveOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.RemoveOperator.html) | Removes a custom operator that was added on the QueryEngine.  
[SetDefaultFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetDefaultFilter.html) | Sets the default filter handler for filters that were not registered.  
[SetDefaultParamFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetDefaultParamFilter.html) | Sets the default filter handler for function filters that were not registered.  
[SetFilterNestedQueryTransformer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetFilterNestedQueryTransformer.html) | Sets a filter's nested query transformer function. This function takes the result of a nested query and extracts the necessary data to compare with the filter.  
[SetGlobalStringComparisonOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetGlobalStringComparisonOptions.html) | Sets global string comparison options. Used for word matching and filter handling (unless overridden by filter).  
[SetNestedQueryHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetNestedQueryHandler.html) | Sets the function that will handle nested queries. Only one handler can be set.  
[SetSearchDataCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetSearchDataCallback.html) | Sets the callback used to fetch the data that is matched against the search words.  
[SetSearchWordMatcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetSearchWordMatcher.html) | Set the search word matching function to be used instead of the default one. Set to null to use the default.  
[TryGetFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.TryGetFilter.html) | Get a filter by its token.  
* * *
