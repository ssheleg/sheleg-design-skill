import { forwardRef } from 'react';
import type { HTMLAttributes, ReactNode } from 'react';

export interface HeadingProps
  extends Omit<HTMLAttributes<HTMLHeadingElement>, 'className'> {
  /** 1 = display (56px, Outfit), 2 = section (44px, Inter), 3 = card head (18px). */
  level?: 1 | 2 | 3;
  /** Visual size — defaults to the level, so existing call sites keep their look. */
  size?: 1 | 2 | 3;
  children: ReactNode;
  className?: string;
}

export const Heading = forwardRef<HTMLHeadingElement, HeadingProps>(function Heading(
  { level = 2, size, className, children, ...rest },
  ref,
) {
  const Tag = `h${level}` as 'h1' | 'h2' | 'h3';
  return (
    <Tag
      ref={ref}
      // The TAG follows the semantic level; the CLASS follows the visual size —
      // an h2 may wear the display size without touching the document outline.
      className={['ch-h', `ch-h--${size ?? level}`, className]
        .filter(Boolean)
        .join(' ')}
      {...rest}
    >
      {children}
    </Tag>
  );
});
