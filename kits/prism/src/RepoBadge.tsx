export interface RepoBadgeProps {
  /** e.g. "45.5k" — a number, not a logo. */
  stars: string;
  repo: string;
  href?: string;
  className?: string;
}

/**
 * Social proof stated as a number in mono rather than as a wall of customer
 * logos — which is the right proof for a project page, and the wrong one for a
 * company page.
 */
export function RepoBadge({ stars, repo, href, className }: RepoBadgeProps) {
  const Tag = href ? 'a' : 'span';
  return (
    <Tag
      className={['pr-repo', className].filter(Boolean).join(' ')}
      {...(href ? { href } : {})}
    >
      <span className="pr-repo__name">{repo}</span>
      <span className="pr-repo__stars">{stars}</span>
    </Tag>
  );
}
