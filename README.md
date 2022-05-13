--user
Kiuwan username

--pass
Kiuwan password

--sourcePath
Directory with code to analyze

--softwareName
Name of the target application

--create
Create software at kiuwan service if not exists

--label
Label for the analysis

--model-name
The model name to use when analyzing

--analysis-scope
The analysis scope. One of [baseline|completeDelivery|partialDelivery].
Defaults to baseline.

--change-request
The change request associated with the delivery to analyze or promote
(implies -as completeDelivery if no other option is specified)

--change-request-status
The change request status. One of [inprogress|resolved]. Defaults to
resolved. Only applies to delivery scopes

--branch-name
The branch name associated with the delivery to analyze (implies --analysis-scope
completeDelivery if no other option is specified)

--promote-to-baseline
Promotes a single delivery to baseline (-n, -l and -cr must be specified) or all pending deliveries (-n must be specified)
Default: false

--wait-for-results
Wait for kiuwan to return complete results once the local analysis has finished
Default: false
