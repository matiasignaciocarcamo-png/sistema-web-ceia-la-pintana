import React from 'react'; export default function StatCard({title,value,caption}){return <article className="stat-card"><p>{title}</p><strong>{value}</strong><small>{caption}</small></article>}
