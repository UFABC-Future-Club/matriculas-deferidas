import settings.mongo_client 

mongo_col = settings.mongo_client.mongo_col 

mongo_col.update(
    {prática: ""}, 
    {$unset: { prática: "", prof_pratica: "" }}
) 

mongo_col.update(
    {teoria: ""},
    {$unset: { teoria: "", prof_teoria: "" }}
)