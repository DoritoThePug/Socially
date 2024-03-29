export default interface User {
  email: string;
  username: string;
  date_joined: string;
  get_profile_picture: string;
  bio: string;
  first_name: string;
  last_name: string;
  liked_posts: number;
  followers: number;
  following: number;
  slug: string;
}
