WITH host_cleansed as 
(
    SELECT * FROM {{ ref("src_hosts") }}
)
select 
host_id,
case 
when host_name is not null then host_name 
when host_name is null then coalesce(host_name,'Anonymous')
end as host_name,
is_superhost,
created_at,
updated_at
from host_cleansed