use mongodb::bson::{oid::ObjectId,DateTime};
use serde::{Serialize,Deserialize}

#[derive(Serialize,Deserialize)]
pub struct User {
    _id: ObjectId,
    username: String,
    first_name: String,
    role_permission: String,
    plan: String,
    email: String,
    password: String
    start_time:DateTime,
}



