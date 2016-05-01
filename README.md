===== Dredd

Judge, Jury, Executioner

= Rest API for Determining Sentiment

Super simple service leveraging python module for NLP Sentiment Analysis

To Test,

    curl http://localhost:4500/api/v1/ -d "text=awesome movie" -X GET


I run as a docker container with a super simple

    docker run --rm -p 4500:4500 undeadops/dredd


