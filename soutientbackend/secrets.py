from dotenv import load_dotenv
import os
load_dotenv()

engine = os.getenv("SUPABASE_ENGINE")
name=os.getenv("SUPABASE_NAME")
user=os.getenv("SUPABASE_USER")
password=os.getenv("SUPABASE_PASSWORD")
host=os.getenv("SUPABASE_HOST")
port=os.getenv("SUPABASE_PORT")
