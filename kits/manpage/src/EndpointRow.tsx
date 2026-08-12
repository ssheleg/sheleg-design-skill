import type { ReactNode } from 'react';

export type Method = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE';

export interface EndpointRowProps {
  method: Method;
  /** The path, set in mono: `/whatsapp/phone-numbers/purchase`. */
  path: string;
  children?: ReactNode;
  /** Drawn as the selected row — the one the surrounding copy is about. */
  selected?: boolean;
  className?: string;
}

export function EndpointRow({ method, path, children, selected = false, className }: EndpointRowProps) {
  return (
    <div
      className={[
        'mp-endpoint',
        selected ? 'mp-endpoint--selected' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      <span className={['mp-endpoint__method', `mp-endpoint__method--${method.toLowerCase()}`].join(' ')}>
        {method}
      </span>
      <code className="mp-endpoint__path">{path}</code>
      {children !== undefined && <span className="mp-endpoint__note">{children}</span>}
    </div>
  );
}
