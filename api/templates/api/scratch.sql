SELECT date,company,product,topic,open_source_project, cumulative_dev FROM ( WITH firstseen AS (
     SELECT Posts."OwnerUserId" as user_id, date_trunc(\'month\', MIN(Posts."CreationDate"::date)) date FROM Posts LEFT  JOIN PostTags on PostTags.PostId = Posts."Id" WHERE "CreationDate"::date >= \'2015-01-01\' AND (PostTags.tag IN   ' + str(row['stackoverflow_tags']) + ') UNION SELECT Posts."OwnerUserId" as user_id, date_trunc(\'month\', MIN(Posts."CreationDate"::date)) date FROM Posts LEFT  JOIN PostTags on PostTags.PostId = Posts."Id" WHERE "CreationDate"::date >= \'2015-01-01\' AND ' + str(row['stackoverflow_search']) + ' GROUP BY 1) 
     
     SELECT   DISTINCT \'' + str(row['company']) + '\' AS company, \'' + str(row['product']) + '\' AS product, \'' + str(row['open_source_project']) + '\' AS open_source_project, \'' + str(row['topic']) + '\' AS topic, date, COUNT(user_id) OVER (ORDER BY date) cumulative_dev FROM firstseen ORDER BY 1) a  GROUP BY date,company,product,topic, open_source_project, cumulative_dev



     SELECT user_id, min(date) as date FROM (SELECT Posts."OwnerUserId" as user_id, date_trunc('month', MIN(Posts."CreationDate"::date)) date FROM Posts LEFT JOIN PostTags on PostTags.PostId = Posts."Id" WHERE "CreationDate"::date >= '2015-01-01' AND (PostTags.tag IN   ' + str(row['stackoverflow_tags']) + ')) GROUP BY 1 UNION SELECT Posts."OwnerUserId" as user_id, date_trunc('month', MIN(Posts."CreationDate"::date)) date FROM Posts LEFT JOIN PostTags on PostTags.PostId = Posts."Id" WHERE "CreationDate"::date >= '2015-01-01' AND ' + str(row['stackoverflow_search']) + ' GROUP BY 1) a 

GROUP BY 1








SELECT
    date,
    company,
    product,
    topic,
    open_source_project,
    cumulative_dev
FROM
    (
        WITH firstseen AS (     SELECT user_id, min(date) as date FROM (SELECT Posts."OwnerUserId" as user_id, date_trunc('month', MIN(Posts."CreationDate"::date)) date FROM Posts LEFT JOIN PostTags on PostTags.PostId = Posts."Id" WHERE "CreationDate"::date >= '2015-01-01' AND (PostTags.tag IN   ' + str(row['stackoverflow_tags']) + ')) GROUP BY 1 UNION SELECT Posts."OwnerUserId" as user_id, date_trunc('month', MIN(Posts."CreationDate"::date)) date FROM Posts LEFT JOIN PostTags on PostTags.PostId = Posts."Id" WHERE "CreationDate"::date >= '2015-01-01' AND ' + str(row['stackoverflow_search']) + ' GROUP BY 1) a 

GROUP BY 1) 
                    
                    
                    
                    
                    SELECT   DISTINCT \'' + str(row ['company']) + '\' AS company, \'' + str(row ['product']) + '\' AS product, \'' + str(row ['open_source_project']) + '\' AS open_source_project, \'' + str(row ['topic']) + '\' AS topic, date, COUNT(user_id) OVER (ORDER BY date) cumulative_dev FROM firstseen ORDER BY 1) a  GROUP BY date,company,product,topic, open_source_project, cumulative_dev