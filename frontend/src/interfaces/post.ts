import user from './user'

export default interface Post {
    id: number
    content: string
    author: user
    date_created: string
    likes: number[]
    get_absolute_url: string
}